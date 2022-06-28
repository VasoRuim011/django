from django.db import models

# Create your models here.


class Funcionario(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField()
