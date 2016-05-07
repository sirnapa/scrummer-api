# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserStory', '0006_userstory_sprint'),
        ('Nota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='userStory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserStory.UserStory'),
        ),
    ]
