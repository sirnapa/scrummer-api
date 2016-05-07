from __future__ import unicode_literals
from actividad.models import actividad
from django.db import models


class flujo (models.Model):
    class Meta:
        verbose_name = 'flujo'
        verbose_name_plural = 'flujos'

    nombre = models.CharField(unique=True, max_length=45)
    actividades = models.ForeignKey(actividad, null=True, blank=True, default=None)
    def __unicode__(self):
        return self.nombre