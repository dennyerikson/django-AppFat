# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-11 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_curso_cur_id_uni'),
    ]

    operations = [
        migrations.AddField(
            model_name='sats',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
