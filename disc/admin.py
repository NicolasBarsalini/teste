from django.contrib import admin
from django import forms
from .models import Pergunta, ESCOLHAS_RESPOSTAS

class PerguntaForm(forms.ModelForm):
    resposta = forms.ChoiceField(
        choices=ESCOLHAS_RESPOSTAS, 
        widget=forms.RadioSelect, 
        initial=3
    )
    
    class Meta:
        model = Pergunta
        fields = '__all__'

class PerguntaAdmin(admin.ModelAdmin):
    form = PerguntaForm  # Usa o formulário personalizado
    list_display = ('texto', 'perfil', 'resposta')  
    list_filter = ('perfil',)  
    search_fields = ('texto',)

admin.site.register(Pergunta, PerguntaAdmin)





