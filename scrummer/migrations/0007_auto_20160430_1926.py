# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 19:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrummer', '0006_auto_20160430_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2016, 4, 30, 19, 26, 8, 103735, tzinfo=utc), verbose_name='Fecha de Fin'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='fechaInicio',
            field=models.DateField(default=datetime.datetime(2016, 4, 30, 19, 26, 8, 103491, tzinfo=utc), verbose_name='Fecha de Inicio'),
        ),
    ]
