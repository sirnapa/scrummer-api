# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla_de_flujo', '0002_auto_20160507_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantilla_de_flujo',
            name='actividades',
        ),
    ]