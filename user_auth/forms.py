from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    first_name = forms.CharField(required=False, label="Primeiro nome")
    last_name = forms.CharField(required=False, label="Último nome")
    
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'telefone',
            'profissao',
            'nivel_educacao',
            'status_educacao',
            'genero',
            'data_nascimento',
            'localizacao',
            'setor'
        ]
        # Aqui estamos definindo que o campo 'genero' é obrigatório.
        widgets = {
            'genero': forms.Select(attrs={'required': True}),
        }
