# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'nota',
                'verbose_name_plural': 'notas',
            },
        ),
    ]