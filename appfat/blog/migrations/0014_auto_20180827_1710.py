# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-27 20:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180824_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sats',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='sats',
            name='published_date',
        ),
    ]
