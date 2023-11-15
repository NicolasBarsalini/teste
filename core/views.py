from django.shortcuts import render, redirect
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html') 
# Create your views here.

#renderizar a pagina sobre e contato
def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def perfil_dominante(request):
    return render(request,'perfis/dominante.html')

def perfil_influente(request):
    return render(request,'perfis/influente.html')

def perfil_estavel(request):
    return render(request,'perfis/estavel.html')

def perfil_cauteloso(request):
    return render(request,'perfis/cauteloso.html')

"""
def redirecionar_cadastro(request):
    return redirect(reverse_lazy('user_auth:cadastro'))  # Note o uso de 'user_auth:cadastro'
""" 
   
