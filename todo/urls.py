from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('set-status/<int:todo_id>/', views.set_completed_todo, name='set_status'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('create/', views.create_todo, name='create_todo'),
    path('update/<int:todo_id>/', views.update_todo, name='update_todo')
]
