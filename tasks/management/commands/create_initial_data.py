from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from tasks.models import Task, Note, SubTask, Priority, Category


class Command(BaseCommand):
    help = "Generate fake data for Task, Note, and SubTask"

    def handle(self, *args, **kwargs):

        fake = Faker()

        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        if not priorities:
            self.stdout.write(
                self.style.ERROR(
                    "Please add Priority records first."
                )
            )
            return

        if not categories:
            self.stdout.write(
                self.style.ERROR(
                    "Please add Category records first."
                )
            )
            return

        tasks = []

        # Create Tasks
        for i in range(10):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),

                description=fake.paragraph(
                    nb_sentences=3
                ),

                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed"
                    ]
                ),

                deadline=timezone.make_aware(
                    fake.date_time_this_month()
                ),

                priority=random.choice(priorities),
                category=random.choice(categories)
            )

            tasks.append(task)

        # Create Notes
        for i in range(20):
            Note.objects.create(
                task=random.choice(tasks),
                content=fake.paragraph(
                    nb_sentences=3
                )
            )

        # Create SubTasks
        for i in range(20):
            SubTask.objects.create(
                parent_task=random.choice(tasks),

                title=fake.sentence(
                    nb_words=5
                ),

                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed"
                    ]
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Fake data created successfully!"
            )
        )