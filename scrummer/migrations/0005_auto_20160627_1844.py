# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrummer', '0004_auto_20160627_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
    ]
