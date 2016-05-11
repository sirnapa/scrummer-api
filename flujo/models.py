from __future__ import unicode_literals
from django.db import models
from proyecto.models import proyecto


class flujo (models.Model):
    class Meta:
        verbose_name = 'flujo'
        verbose_name_plural = 'flujos'

    nombre = models.CharField(unique=True, max_length=45)
    proyecto = models.ForeignKey(proyecto, null=True, blank=True, default=None)

    def __unicode__(self):
        return self.nombre