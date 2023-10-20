from django.db import models

# Defina as escolhas para as respostas
ESCOLHAS_RESPOSTAS = (
    (5, 'Concordo Muito'),
    (4, 'Concordo'),
    (3, 'Neutro'),
    (2, 'Discordo'),
    (1, 'Discordo Muito'),
)

class Pergunta(models.Model):
    #transformar as perguntas em um modelo de escala de resposta likert:
    
    texto = models.CharField(max_length=255)
    perfil = models.CharField(max_length=10, choices=[('d', 'Dominante'), ('i', 'Influente'), ('s', 'Estabilidade'), ('c', 'Conformado')])
    resposta = models.IntegerField(choices=ESCOLHAS_RESPOSTAS, default=3)  # Use o campo IntegerField com as escolhas

    def __str__(self):
        return self.texto


class ResultadoDISC(models.Model):
    dominante = models.FloatField(default=0)
    influente = models.FloatField(default=0)
    estabilidade = models.FloatField(default=0)
    conformado = models.FloatField(default=0)
    
    @property
    def perfil_mais_alto(self):
        valores = {
            'd': self.dominante,
            'i': self.influente,
            's': self.estabilidade,
            'c': self.conformado
        }
        return max(valores, key=valores.get)
