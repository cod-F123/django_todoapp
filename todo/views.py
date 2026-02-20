from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Todo

# Create your views here.

@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo/index.html',{"todos": todos})
