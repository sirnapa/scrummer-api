# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='plantilla_de_flujo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, unique=True)),
                ('actividades', models.ManyToManyField(blank=True, default=None, null=True, to='actividad.actividad')),
            ],
            options={
                'verbose_name': 'plantilla_de_flujo',
                'verbose_name_plural': 'plantillas_de_flujo',
            },
        ),
    ]