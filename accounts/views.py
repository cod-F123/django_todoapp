from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib import messages
from .froms import UserRegisterForm
from .decorators import anonamous_required

# Create your views here.

User = get_user_model()

@anonamous_required
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return redirect(reverse('accounts:login_user',query={"error_message": 'username not exist or passwrod wrong !'}))
        
        login(request=request, user=user)
        messages.success(request, 'login successfully !.')
        
        return redirect('todo:index')
    
    error_message = request.GET.get('error_message',None)
    return render(request, 'accounts/login.html',{"error_message": error_message})


def logout_user(request):
    logout(request)
    
    messages.success(request, 'logout successfuly !.')
    
    return redirect('accounts:login_user')


def register_user(request):
    pass