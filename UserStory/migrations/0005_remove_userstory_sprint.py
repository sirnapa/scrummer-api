# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserStory', '0004_userstory_sprint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='sprint',
        ),
    ]