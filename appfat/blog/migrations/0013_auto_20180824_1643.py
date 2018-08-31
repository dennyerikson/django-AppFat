# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-24 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_sats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boleto', models.CharField(max_length=150)),
                ('data', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conecta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_vaga', models.TextField(max_length=300)),
                ('con_id', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conv_title', models.TextField(max_length=100)),
                ('conv_info', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cuso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_nome', models.CharField(max_length=150)),
                ('cur_status', models.CharField(max_length=150)),
                ('cur_prof', models.CharField(max_length=150)),
                ('cur_contato', models.CharField(max_length=150)),
                ('cur_nome_coor', models.CharField(max_length=150)),
                ('cur_cont_coor', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala_dis', models.TextField(max_length=300)),
                ('sala_dados', models.TextField(max_length=150)),
                ('sala_sala', models.TextField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='info_title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]