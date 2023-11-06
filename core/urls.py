from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    #criar path da pagina sobre e contato..html:
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    #path('redirecionar_cadastro/', views.redirecionar_cadastro, name='redirecionar_cadastro'),

]