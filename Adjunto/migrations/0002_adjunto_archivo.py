# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adjunto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjunto',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
