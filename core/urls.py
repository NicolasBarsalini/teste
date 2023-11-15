from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    #criar path da pagina sobre e contato..html:
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('perfil_dominante/', views.perfil_dominante, name='perfil_dominante'),
    path('perfil_influente/', views.perfil_influente, name='perfil_influente'),
    path('perfil_estavel/', views.perfil_estavel, name='perfil_estavel'),
    path('perfil_cauteloso/', views.perfil_cauteloso, name='perfil_cauteloso'),

]