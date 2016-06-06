from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

class permiso (models.Model):
    class Meta:
        verbose_name = 'permiso'
        verbose_name_plural = 'permisos'

    nombre = models.CharField(unique=True, max_length=45)


def __unicode__(self):
 return self.nombre