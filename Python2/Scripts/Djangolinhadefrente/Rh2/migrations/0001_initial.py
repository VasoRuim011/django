# Generated by Django 4.0.5 on 2022-06-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('nome', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=30)),
                ('departamento', models.CharField(max_length=30)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
