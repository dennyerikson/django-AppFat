# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-27 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180727_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dis_curso',
        ),
        migrations.AddField(
            model_name='aluno',
            name='alu_curso',
            field=models.CharField(default='Analise e Desenvolvimento de Sistemas', max_length=20),
            preserve_default=False,
        ),
    ]
