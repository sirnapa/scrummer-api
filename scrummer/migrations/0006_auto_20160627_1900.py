# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 19:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrummer', '0005_auto_20160627_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='observacion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
    ]
