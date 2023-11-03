from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('add/', views.insert_task, name='insert_task'),
    path('view/<int:id>/', views.details_task, name='details_task'),
    path('update/<int:id>/', views.modify_task, name='modify_task'),
    path('delete/<int:id>/', views.destroy_task, name='destroy_task'),
    path('search/<key>/', views.search_tasks, name='search_tasks'),
    path('filter/<status>/', views.filter_tasks, name='filter_tasks'),
]
