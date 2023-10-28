""" 
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
"""
#acima a versoo antiga de autenticação sem o allauth

#abaixo a versão com o allauth
from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser

class CustomAllauthSignupForm(SignupForm):
    first_name = forms.CharField(required=False, label="Primeiro nome")
    last_name = forms.CharField(required=False, label="Último nome")
    telefone = forms.CharField(max_length=15, required=False)
    profissao = forms.CharField(max_length=100, required=False)
    #nivel_educacao = forms.ChoiceField(choices=CustomUser.NIVEL_EDUCACAO_CHOICES, required=False)
    #status_educacao = forms.ChoiceField(choices=CustomUser.STATUS_EDUCACAO_CHOICES, required=False)
    #genero = forms.ChoiceField(choices=CustomUser.GENERO_CHOICES, widget=forms.Select(attrs={'required': True}))
    data_nascimento = forms.DateField(required=False)
    cidade = forms.CharField(max_length=100, required=False)
    #setor = forms.CharField(max_length=100, required=False)

    def save(self, request):
        user = super(CustomAllauthSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.telefone = self.cleaned_data['telefone']
        user.profissao = self.cleaned_data['profissao']
        user.nivel_educacao = self.cleaned_data['nivel_educacao']
        user.status_educacao = self.cleaned_data['status_educacao']
        user.genero = self.cleaned_data['genero']
        user.data_nascimento = self.cleaned_data['data_nascimento']
        user.localizacao = self.cleaned_data['localizacao']
        user.setor = self.cleaned_data['setor']
        user.save()
        return user
