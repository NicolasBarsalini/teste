from django.shortcuts import render, redirect
from django.contrib.auth import logout
#from django.contrib.auth import authenticate, login
#from .forms import CustomUserForm
#from django.http import HttpResponse
from disc.models import ResultadoDISC
from disc.views import ResultadoView


app_name = 'user_auth'


"""
def register(request): # View para o cadastro de usuários
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('core:index')  # Substituir pelo nome da view para onde redirecionar após o cadastro
    else:
        form = CustomUserForm() # Se não for POST, exibe o formulário para o usuário preencher

    return render(request, 'cadastro.html', {'form': form})
"""
#acima a versão antiga de autenticação sem o allauth

"""
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_auth:perfil')
        else:
            return HttpResponse('Credenciais inválidas')
    else:
        return render(request, 'login.html')
    
"""
#acima login sem a versão allauth


# user_auth/views.py
def perfil(request):
    resultado_disc = request.user.resultado_disc if request.user.is_authenticated and request.user.resultado_disc else None
    perfil_mais_alto = resultado_disc.perfil_mais_alto if resultado_disc else None

    PERFIL_MAP = {
        'd': 'Dominante',
        'i': 'Influente',
        's': 'Estabilidade',
        'c': 'Conformado'
    }
    
    PERFIL_DESCRICAO = {

    'd': 'Perfil Dominante: Indivíduos com características assertivas e orientados para resultados. São diretos, assertivos e orientados para metas, frequentemente assumindo o controle e tomando decisões rapidamente.',
    'i': 'Perfil Influente: Pessoas comunicativas e sociáveis, que gostam de interações sociais. São otimistas, persuasivos e gostam de influenciar os outros. Tendem a ser expressivos e energéticos.',
    's': 'Perfil Estabilidade: Indivíduos estáveis e consistentes, valorizam a harmonia e a segurança. São pacientes, leais e preferem ambientes mais previsíveis. Tendem a ser calmos e amigáveis.',
    'c': 'Perfil Conformado: Pessoas precisas e analíticas, que valorizam a precisão e os detalhes. São cautelosos, meticulosos e buscam a exatidão. Tendem a ser lógicos e focados em procedimentos.'
    }

    LOCAIS_TRABALHO = {
        'd': 'Ambientes onde a liderança assertiva e a tomada de decisão rápida são valorizadas, como cargos de gestão, empreendedorismo ou áreas competitivas como vendas e negociações.',
        'i': 'Trabalhos que envolvam interação social e comunicação, como marketing, relações públicas, áreas de entretenimento, vendas e cargos que exijam networking.',
        's': 'Ambientes com equilíbrio, estabilidade e foco em relações interpessoais, como serviços sociais, áreas de suporte ao cliente, administração e cargos que demandem paciência e cooperação.',
        'c': 'Atividades que valorizem precisão e análise detalhada, como engenharia, desenvolvimento de software, áreas financeiras, pesquisa científica e cargos que demandem rigor técnico e meticulosidade.'
    }

    context = {
        'resultado_disc': resultado_disc,
        'perfil_mais_alto': PERFIL_MAP.get(perfil_mais_alto, ""),
        'descricao_perfil': PERFIL_DESCRICAO.get(perfil_mais_alto, ""),
        'locais_trabalho': LOCAIS_TRABALHO.get(perfil_mais_alto, "")
    }
    return render(request, 'perfil.html', context)



def user_logout(request):
    logout(request)
    return redirect('core:index')