from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser
from disc.models import ResultadoDISC

class CustomAllauthSignupForm(SignupForm):
    first_name = forms.CharField(required=False, label="Primeiro nome")
    last_name = forms.CharField(required=False, label="Último nome")
    telefone = forms.CharField(max_length=15, required=False)
    profissao = forms.CharField(max_length=100, required=False)
    #nivel_educacao = forms.ChoiceField(choices=CustomUser.NIVEL_EDUCACAO_CHOICES, required=False)
    #status_educacao = forms.ChoiceField(choices=CustomUser.STATUS_EDUCACAO_CHOICES, required=False)
    #genero = forms.ChoiceField(choices=CustomUser.GENERO_CHOICES, widget=forms.Select(attrs={'required': True}))
    data_nascimento = forms.DateField(required=False)
    localizacao = forms.CharField(max_length=100, required=False)
    #setor = forms.CharField(max_length=100, required=False)

    def save(self, request):
        user = super(CustomAllauthSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.telefone = self.cleaned_data['telefone']
        user.profissao = self.cleaned_data['profissao']
        #user.nivel_educacao = self.cleaned_data['nivel_educacao']
        #user.status_educacao = self.cleaned_data['status_educacao']
        #user.genero = self.cleaned_data['genero']
        user.data_nascimento = self.cleaned_data['data_nascimento']
        user.localizacao = self.cleaned_data['localizacao']
        #user.setor = self.cleaned_data['setor']
        user.save()  # Adicione esta linha
        
        resultado_disc = ResultadoDISC.objects.create(
            dominante=0,
            influente=0,
            estabilidade=0,
            conformado=0
        ) 
        # Criação do resultado do teste
        user.resultado_disc = resultado_disc  # Atribuição do resultado ao usuário
        user.save()  # Salvando o usuário
        
        return user
