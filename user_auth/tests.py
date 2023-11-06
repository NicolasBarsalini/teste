from django.test import TestCase

# Create your tests here.
"""
Etapas para a configuração dos testes
Configuração Inicial:

Garantir que o django-allauth esteja corretamente configurado e funcionando no seu projeto.
Certificar-se de que o aplicativo disc esteja integrado ao seu sistema de autenticação de usuário.
Criação de Fixtures:

Preparar um conjunto de dados de teste (conhecidos como "fixtures") que podem ser usados para popular o banco de dados durante os testes. Isso pode incluir usuários de teste, dados de teste DISC, etc.
Escrever TestCases:

Escrever uma classe de TestCase que herda de django.test.TestCase.
Utilizar o Client de teste do Django para simular um usuário se cadastrando no sistema.
Testar o fluxo de autenticação e registro fornecido pelo django-allauth.
Após o registro e autenticação, testar a funcionalidade do aplicativo disc, submetendo as respostas do teste DISC.
Verificar se o resultado do teste DISC é atribuído corretamente ao usuário.
Mocking:

Em alguns casos, você pode precisar usar mocking para simular partes do sistema que são externas ou que você não quer executar durante os testes (como o envio de e-mails).
Informações Necessárias
O modelo do seu usuário e como ele está integrado com o django-allauth.
O modelo ou método que lida com os resultados do teste DISC.
O fluxo de dados esperado desde o registro até a atribuição do resultado do teste DISC.
Qualquer outro componente específico do seu sistema que interaja com o processo de registro e testes.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from disc.models import Pergunta, ResultadoDISC
from disc.forms import QuestionnaireForm
from user_auth.forms import CustomAllauthSignupForm

User = get_user_model()

class UserAuthAndDiscIntegrationTest(TestCase):
    def setUp(self):
        # Precisamos criar algumas perguntas de exemplo para o teste DISC
        Pergunta.objects.create(texto='Pergunta 1', perfil='d')
        Pergunta.objects.create(texto='Pergunta 2', perfil='i')
        Pergunta.objects.create(texto='Pergunta 3', perfil='s')
        Pergunta.objects.create(texto='Pergunta 4', perfil='c')

    def test_user_registration_and_disc_completion(self):
        # Dados de cadastro para um novo usuário
        user_data = {
            'username': 'novousuario',
            'password1': 'senha12345',
            'password2': 'senha12345',
            'email': 'teste@teste.com'
        }

        # Registrar um novo usuário
        response = self.client.post(reverse('account_signup'), user_data)
        self.assertEqual(response.status_code, 302)  # Espera-se um redirecionamento após o cadastro

        # Autenticar o usuário
        self.client.login(username='novousuario', password='senha12345')

        # Obter as perguntas para gerar as respostas do teste DISC
        perguntas = Pergunta.objects.all()
        disc_test_data = {'pergunta_%d' % pergunta.id: 3 for pergunta in perguntas}  # Resposta 'Neutro' para todas

        # Submeter as respostas do teste DISC
        response = self.client.post(reverse('disc:teste_disc'), disc_test_data)
        self.assertEqual(response.status_code, 302)  # Espera-se um redirecionamento após submeter o teste

        # Verificar se o resultado do teste DISC foi associado ao usuário
        user = User.objects.get(username='novousuario')
        self.assertIsNotNone(user.resultado_disc)  # O usuário deve ter um resultado DISC associado

        # Verificar se o perfil mais alto foi calculado corretamente
        self.assertEqual(user.resultado_disc.perfil_mais_alto, 'd')  # 'd' seria o perfil mais alto com as respostas neutras

