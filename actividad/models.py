from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from flujo.models import flujo
class actividad (models.Model):

    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'
        unique_together = ('nombre', 'flujo',)
        unique_together = ('flujo', 'orden',)
    nombre = models.CharField( max_length=45)
    orden = models.IntegerField()
    flujo = models.ForeignKey(flujo, null=False, blank=False, default=None)



def __unicode__(self):
 return self.nombre