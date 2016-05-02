from __future__ import unicode_literals
from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    descripcion = models.CharField(max_length=50, verbose_name='Descripcion')
