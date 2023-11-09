from django.urls import path
from . import views
from .views import QuestionnaireView, ResultadoView

app_name = 'disc'

urlpatterns = [
    path('teste_disc/', QuestionnaireView.as_view(), name='teste_disc'),
    path('resultado/<int:pk>/', ResultadoView.as_view(), name='resultado'),
    path('estatisticas/', views.estatisticas_disc, name='estatisticas-disc'),


]