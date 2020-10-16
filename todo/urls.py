from django.urls import path
from todo import views

urlpatterns = [
    path('', views.list_tasks, name="list_tasks"),
    path('remove/<int:pk>/', views.remove_task, name="remove_task"),
    path('toggle/<int:pk>/', views.toggle_task, name="toggle_task"),
]
