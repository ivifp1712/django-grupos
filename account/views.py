from email.mime import message
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/todos')
    else: 
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def user(request):
    if request.user.is_authenticated == False:
        return redirect('/login/')
    else:
        return render(request, 'user.html')

def login(request):
    if request.user.is_authenticated == True:
        return redirect('/user/')
    else:
        return render(request, 'login.html')