from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
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
        
        if user is not None:
            messages.error(request, 'username not exist or passwrod wrong !')
            return redirect('accounts:login_user')
        
        login(request=request, user=user)
        messages.success(request, 'login successfully !.')
        
        return redirect('todo:index')
    
    return render(request, 'accounts/login.html',{})


def logout_user(request):
    logout(request)
    
    messages.success(request, 'logout successfuly !.')
    
    return redirect('accounts:login_user')