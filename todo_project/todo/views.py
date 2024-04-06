from rest_framework import generics, permissions
from .models import TodoItem
from .serializers import TodoItemSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class TodoListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list_view(request):
    todo_items = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todo_items': todo_items})

@login_required
def update_todo_view(request, pk):
    todo_item = TodoItem.objects.get(pk=pk)
    if request.method == 'POST':
        todo_item.content = request.POST['content']
        todo_item.save()
        return redirect('todo_list')
    return render(request, 'update_todo.html', {'todo_item': todo_item})

@login_required
def delete_todo_view(request, pk):
    todo_item = TodoItem.objects.get(pk=pk)
    if request.method == 'POST':
        todo_item.delete()
        return redirect('todo_list')
    return render(request, 'delete_todo.html', {'todo_item': todo_item})
