# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0002_auto_20160605_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='rol',
            field=models.SmallIntegerField(choices=[(1, 'DESARROLLADOR'), (2, 'SCRUM_MASTER'), (3, 'ADMINISTRADOR')], default=3),
        ),
    ]