# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-08 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_conecta_con_id_cur'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='cur_id_uni',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
