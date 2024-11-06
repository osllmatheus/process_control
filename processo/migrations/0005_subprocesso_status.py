# Generated by Django 5.1.2 on 2024-11-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0004_remove_processo_subprocesso_subprocesso_processo'),
    ]

    operations = [
        migrations.AddField(
            model_name='subprocesso',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('A', 'Em Andamento'), ('C', 'Concluído'), ('X', 'Cancelado')], default='P', max_length=1),
        ),
    ]
