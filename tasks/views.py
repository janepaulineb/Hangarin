from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Priority, Category, Task, Note, SubTask
from tasks.forms import PriorityForm, CategoryForm, TaskForm, NoteForm, SubTaskForm
from django.db.models import Q
from django.urls import reverse_lazy
paginate_by = 5

class HomePageView(ListView) :
    model = Priority
    context_object_name = 'home'
    template_name = "home.html" 

#PRIORITY
class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy('priority-list')
class PriorityList(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = "priority_list.html"
    paginate_by = 5
    ordering = ["prior_name"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(prior_name__icontains=query)
            )
        return qs
    """def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"""

class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy('priority-list')
class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = "priority_del.html"
    success_url = reverse_lazy('priority-list')


#CATEGORY
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy('category-list')
class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = "category_list.html"
    paginate_by = 5
    ordering = ["name"]

    def get_queryset(self):
            qs = super().get_queryset()
            query = self.request.GET.get('q')
            if query:
                qs = qs.filter(
                    Q(name__icontains=query)
                )
            return qs

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy('category-list')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_del.html"
    success_url = reverse_lazy('category-list')

#TASK
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy('task-list')
class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = "task_list.html"
    paginate_by = 5
    ordering = ["title"]

    def get_queryset(self):
            qs = super().get_queryset()
            query = self.request.GET.get('q')
            if query:
                qs = qs.filter(
                    Q(title__icontains=query) |
                    Q(description__icontains=query)
                )
            return qs
    def get_ordering(self):
            allowed = ["title","status","priority__prior_name","category__name","deadline"]
            sort_by = self.request.GET.get("sort_by")
            if sort_by in allowed:
                return sort_by
            return "title"

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy('task-list')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_del.html"
    success_url = reverse_lazy('task-list')

#NOTES
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy('note-list')
class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = "note_list.html"
    paginate_by = 5
    ordering = ["task__title"]

    def get_queryset(self):
            qs = super().get_queryset()
            query = self.request.GET.get('q')
            if query:
                qs = qs.filter(
                    Q(content__icontains=query)
                )
            return qs
    """def get_ordering(self):
        allowed = ["task","created_at"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "task"""

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy('note-list')
class NoteDeleteView(DeleteView):
    model = Note
    template_name = "note_del.html"
    success_url = reverse_lazy('note-list')

#SUBTASK
class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy('subtask-list')
class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = "subtask_list.html"
    paginate_by = 5
    ordering = ["title"]

    def get_queryset(self):
            qs = super().get_queryset()
            query = self.request.GET.get('q')
            if query:
                qs = qs.filter(
                    Q(title__icontains=query)
                )
            return qs
    def get_ordering(self):
                allowed = ["title","status","parent_task__title"]
                sort_by = self.request.GET.get("sort_by")
                if sort_by in allowed:
                    return sort_by
                return "title"

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy('subtask-list')
class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = "subtask_del.html"
    success_url = reverse_lazy('subtask-list')