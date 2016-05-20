# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrummer', '0002_usuario_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='observacion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
