from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html') 
# Create your views here.
def redirecionar_cadastro(request):
    # Redirecionar para a página de cadastro do app "login"
    return redirect(reverse('usuario:cadastrar_usuario'))
