# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla_de_flujo', '0004_plantilla_de_flujo_actividades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantilla_de_flujo',
            name='actividades',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
