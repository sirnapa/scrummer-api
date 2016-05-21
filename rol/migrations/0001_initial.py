# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('0', 'DESARROLLADOR'), ('1', 'SCRUM_MASTER'), ('2', 'ADMINISTRADOR')], default=0, max_length=1)),
                ('permisos_del_rol', models.ManyToManyField(blank=True, help_text='Especifica permisos del rol', related_name='rol_set', related_query_name='user', to='auth.Permission', verbose_name='permisos_del_rol')),
                ('proyecto', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyecto')),
            ],
            options={
                'verbose_name': 'rol',
                'verbose_name_plural': 'roles',
            },
        ),
    ]
