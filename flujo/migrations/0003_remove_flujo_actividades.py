# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 22:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujo', '0002_auto_20160507_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flujo',
            name='actividades',
        ),
    ]