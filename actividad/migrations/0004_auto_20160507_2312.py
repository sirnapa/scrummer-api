# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0003_actividad_flujo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='nombre',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='orden',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='actividad',
            unique_together=set([('flujo', 'orden')]),
        ),
    ]
