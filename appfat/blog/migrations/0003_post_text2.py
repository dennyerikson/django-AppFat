# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-11 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text2',
            field=models.TextField(default='teste'),
            preserve_default=False,
        ),
    ]
