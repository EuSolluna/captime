from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Substitua 'home' pelo nome da sua página inicial
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})