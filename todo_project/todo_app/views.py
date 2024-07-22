# todo_app/views.py
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Welcome to the To-Do List App</h1>")

def index(request):
    return render(request, 'index.html')

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
