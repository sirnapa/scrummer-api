# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrummer', '0004_auto_20160430_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fechaFin',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Fin'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fechaInicio',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio'),
        ),
    ]
