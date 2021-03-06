# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-27 14:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20180716_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alu_cpf', models.CharField(max_length=11)),
                ('alu_ra', models.CharField(max_length=20)),
                ('alu_nome', models.CharField(max_length=200)),
                ('alu_tel', models.CharField(max_length=30)),
                ('alu_cel', models.CharField(max_length=30)),
                ('alu_email', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('alu_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_informacao', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('info_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_cpf', models.CharField(max_length=11)),
                ('status_status', models.TextField()),
                ('status_bolsa', models.TextField()),
                ('status_ajuste', models.TextField()),
                ('status_card', models.TextField()),
                ('status_rematricula', models.TextField()),
                ('status_boleto', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('status_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='dis_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='texto4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='dis_bloco',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='dis_cpf',
            field=models.CharField(default=' ', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='dis_curso',
            field=models.CharField(default=' ', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='dis_data',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='dis_disciplina',
            field=models.CharField(default=' ', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='dis_sala',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='dis_status',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
