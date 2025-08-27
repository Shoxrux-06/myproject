from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
