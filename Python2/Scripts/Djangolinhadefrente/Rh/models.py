from django.db import models

# Create your models here.


class Funcionario(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField()
    cargo = models.CharField()
    departamento = models.CharField()
    salario = models.DecimalField()
    data_nascimento = models.DateField()
