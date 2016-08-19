# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0011_auto_20160628_1630'),
        ('scrummer', '0006_auto_20160627_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='observacion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rol.rol'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='usuario', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]