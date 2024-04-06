from django.urls import path
from .views import TodoListView, TodoDetailView
from . import views

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.todo_list_view, name='todo_list'),
    path('todo/<int:pk>/update/', views.update_todo_view, name='update_todo'),
    path('todo/<int:pk>/delete/', views.delete_todo_view, name='delete_todo'),
]

