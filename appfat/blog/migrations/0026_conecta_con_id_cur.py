# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-14 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20180914_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='conecta',
            name='con_id_cur',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
