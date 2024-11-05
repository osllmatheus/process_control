# Generated by Django 5.1.2 on 2024-11-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0002_rename_subprocessos_processo_subprocesso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subprocesso',
            name='parent_subprocesso',
        ),
        migrations.AddField(
            model_name='subprocesso',
            name='parent_subprocesso',
            field=models.ManyToManyField(blank=True, related_name='subprocessos_filhos', to='processo.subprocesso'),
        ),
    ]
