# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]