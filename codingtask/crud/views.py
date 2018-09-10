from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

# Create your views here.

def index(request):
    return render(request, 'index.html')    


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def logout(request):
    auth_logout(request)
    return redirect(reverse('index'))