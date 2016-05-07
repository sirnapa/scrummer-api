from __future__ import unicode_literals

from django.db import models

class actividad (models.Model):
    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'

    nombre = models.CharField(unique=True, max_length=45)
    orden = models.IntegerField(unique=True,max_length=45)
    def __unicode__(self):
        return self.nombre