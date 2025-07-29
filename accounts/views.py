
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')  # Redirect to account page after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def account(request):
    return render(request, 'account.html')
