# Generated by Django 4.0.5 on 2022-07-05 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh2', '0003_departamento_alter_funcionario_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(choices=[('ES', 'Estagiario'), ('AS', 'Assistente'), ('JR', 'Junior'), ('PL', 'Pleno'), ('SR', 'Senior'), ('GR', 'Gerente')], max_length=20),
        ),
    ]