# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrummer', '0003_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Usuario',
        ),
    ]
