from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserForm

app_name = 'user_auth'

def register(request): # View para o cadastro de usuários
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('user_auth:login')  # Substitua pelo nome da view para onde você quer redirecionar após o cadastro
    else:
        form = CustomUserForm()

    return render(request, 'cadastro.html', {'form': form})

def user_login(request):
    # Implemente sua lógica de login aqui
    pass

