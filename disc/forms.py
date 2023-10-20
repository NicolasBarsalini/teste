from django import forms
from .models import Pergunta, ESCOLHAS_RESPOSTAS
import random

class QuestionnaireForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        perguntas = list(Pergunta.objects.all())
        random.shuffle(perguntas)
        for pergunta in perguntas:
            self.fields[f'pergunta_{pergunta.id}'] = forms.ChoiceField(
                label=pergunta.texto,
                choices=ESCOLHAS_RESPOSTAS,
                widget=forms.RadioSelect
            )