from django.urls import path
from todolist.views import delete_task, show_todolist, register, login_user, logout_user, create_task, toggle_task_status, delete_task, get_json, create_task_ajax, delete_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('toggle-status/<int:id>', toggle_task_status, name='toggle_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('json/', get_json, name='get_json'),
    path('add/', create_task_ajax, name='add'),
    path('delete/<int:id>', delete_task_ajax, name='delete'),
]

