from django.urls import path
from . import views
from .views import QuestionnaireView, ResultadoView

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('redirecionar-cadastro/', views.redirecionar_cadastro, name='redirecionar_cadastro'),

]