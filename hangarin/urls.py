"""
URL configuration for hangarin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import HomePageView
from tasks.views import PriorityCreateView, PriorityList, PriorityUpdateView, PriorityDeleteView
from tasks.views import CategoryCreateView, CategoryList, CategoryUpdateView, CategoryDeleteView
from tasks.views import TaskCreateView, TaskList, TaskUpdateView, TaskDeleteView
from tasks.views import NoteCreateView, NoteList, NoteUpdateView, NoteDeleteView
from tasks.views import SubTaskCreateView, SubTaskList, SubTaskUpdateView, SubTaskDeleteView
from tasks import views

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view(), name='home'),
    path('organization_list', PriorityList.as_view(), name='priority-list'),
]'''

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("accounts/",include("allauth.urls")), #allauth routes
    path('', views.HomePageView.as_view(), name='home'),

    path('priority-list', PriorityList.as_view(), name='priority-list'),
    path('priority-list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('priority-list/<pk>', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority-list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),

    path('category-list', CategoryList.as_view(), name='category-list'),
    path('category/add', CategoryCreateView.as_view(), name='category-add'),
    path('category/<pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),

    path('task', TaskList.as_view(), name='task-list'),
    path('task/add', TaskCreateView.as_view(), name='task-add'),
    path('task/<pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),

    path('note', NoteList.as_view(), name='note-list'),
    path('note/add', NoteCreateView.as_view(), name='note-add'),
    path('note/<pk>', NoteUpdateView.as_view(), name='note-update'),
    path('note/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'),

    path('subtask', SubTaskList.as_view(), name='subtask-list'),
    path('subtask/add', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask/<pk>', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),
]
