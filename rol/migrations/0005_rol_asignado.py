# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 23:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rol', '0004_auto_20160605_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]