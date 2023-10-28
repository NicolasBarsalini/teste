from django.urls import path, include
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),  # certifique-se que esta linha exista
    path('logout/', views.user_logout, name='logout'),  # Nova linha
    #path('cadastro/', views.register, name='cadastro'),
    #path('login/', views.user_login, name='login'),
    # ... suas outras URLs
]
