from random import choices
from time import time
from django.db import models

# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=20)


    def __str__(self):
        return self.nome


class Funcionario(models.Model):
        
    CARGOS = [
        ('ES', 'Estagiario'), 
        ('AS', 'Assistente'),
        ('JR', 'Junior'),
        ('PL', 'Pleno'),
        ('SR', 'Senior'),
        ('GR', 'Gerente'),
    ]

    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20, choices=CARGOS)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField(null=True)
    horas_trabalhadas = models.TimeField(choices=time)

    def __str__(self):
        return self.nome

    def valor_hora:

            valor_hora = float(input("Digite o valor ganho por hora de trabalho: "))
            horas_trabalhadas = float(input("Digite o valor de horas trabalhadas neste mês: "))
            pagamento = valor_hora * horas_trabalhadas
            print("Você trabalhou por",horas_trabalhadas,"horas.")
            print("O valor da hora trabalhada é de R$",valor_hora)
            print("O pagamento que deve ser recebido é de: R$",pagamento)