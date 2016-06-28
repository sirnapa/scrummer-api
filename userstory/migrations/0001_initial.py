# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 22:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nota', '0001_initial'),
        ('adjunto', '0001_initial'),
        ('flujo', '0001_initial'),
        ('historial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userstory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=150)),
                ('valorNegocio', models.SmallIntegerField(default=0)),
                ('tiempoEstimado', models.SmallIntegerField(default=0)),
                ('tiempoReal', models.SmallIntegerField(default=0)),
                ('prioridad', models.CharField(choices=[('0', 'Baja'), ('1', 'Media'), ('2', 'Alta')], default=0, max_length=1)),
                ('adjunto', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='adjunto.adjunto')),
                ('flujo', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='flujo.flujo')),
                ('historial', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='historial.historial')),
                ('nota', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='nota.nota')),
                ('sprint', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sprint.sprint')),
                ('usuario', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'userstory',
                'verbose_name_plural': 'userstorys',
            },
        ),
    ]
