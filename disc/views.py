from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from disc.models import Pergunta, ResultadoDISC
from .forms import QuestionnaireForm
from django.views.generic import DetailView


"""def form_valid(self, form):
    # Dicionário para armazenar as pontuações
    pontuacoes = {'d': 0, 'i': 0, 's': 0, 'c': 0}
    contagem = {'d': 0, 'i': 0, 's': 0, 'c': 0}
    
    # Processar as respostas
    for name, value in form.cleaned_data.items():
        pergunta_id = int(name.split('_')[1])
        pergunta = Pergunta.objects.get(pk=pergunta_id)
        pontuacoes[pergunta.perfil] += int(value)
        contagem[pergunta.perfil] += 1"""
    
# Calculando a média
class QuestionnaireView(FormView): #antigo PerguntaView
        form_class = QuestionnaireForm
        template_name = 'teste_disc.html'
        success_url = None

        def form_valid(self, form):
            # Dicionário para armazenar as pontuações
            pontuacoes = {'d': 0, 'i': 0, 's': 0, 'c': 0}
            contagem = {'d': 0, 'i': 0, 's': 0, 'c': 0}

            # Processar as respostas
            for name, value in form.cleaned_data.items():
                pergunta_id = int(name.split('_')[1])
                pergunta = Pergunta.objects.get(pk=pergunta_id)
                pontuacoes[pergunta.perfil] += int(value)
                contagem[pergunta.perfil] += 1

            # Calculando a média
            medias = {perfil: pontuacoes[perfil]/contagem[perfil] for perfil in pontuacoes}

            # Salvar as médias no modelo ResultadoDISC
            resultado = ResultadoDISC(
                dominante=medias['d'],
                influente=medias['i'],
                estabilidade=medias['s'],
                conformado=medias['c']
            )
            resultado.save()
            
        # Associa o resultado DISC ao usuário se ele estiver logado
            if self.request.user.is_authenticated:
                self.request.user.resultado_disc = resultado
                self.request.user.save()

            # Redirecionando para a página de resultados com o ID do resultado
                self.success_url = reverse_lazy('disc:resultado', kwargs={'pk': resultado.id})

            return super(QuestionnaireView, self).form_valid(form)


#mostrando o resultado

class ResultadoView(DetailView):
    
    model = ResultadoDISC
    template_name = 'resultado_disc.html'
    
    def get_context_data(self, **kwargs):
        
        PERFIL_MAP = {
        'd': 'Dominante',
        'i': 'Influente',
        's': 'Estabilidade',
        'c': 'Conformado'
    }
        PERFIL_DESCRICAO = {
        'd': 'Descrição para perfil Dominante', # aqui deverão ser inseridos os textos de cada perfil
        'i': 'Descrição para perfil Influente',
        's': 'Descrição para perfil Estabilidade',
        'c': 'Descrição para perfil Conformado'
    }

        LOCAIS_TRABALHO = {
        'd': 'Locais ideais para perfil Dominante', #aqui deverão ser inseridos os locais de trabalho de cada perfil
        'i': 'Locais ideais para perfil Influente',
        's': 'Locais ideais para perfil Estabilidade',
        'c': 'Locais ideais para perfil Conformado'
    }

        
        context = super().get_context_data(**kwargs)
        inicial_perfil_mais_alto = self.object.perfil_mais_alto
        context['perfil_mais_alto'] = PERFIL_MAP[inicial_perfil_mais_alto]
        context['descricao_perfil'] = PERFIL_DESCRICAO[inicial_perfil_mais_alto]
        context['locais_trabalho'] = LOCAIS_TRABALHO[inicial_perfil_mais_alto]
    
        return context
