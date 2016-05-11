from __future__ import unicode_literals

from django.db import models



class plantilla_de_flujo (models.Model):
    """Clase Plantilla de flujo"""
    class Meta:
        verbose_name = 'plantilla_de_flujo'
        verbose_name_plural = 'plantillas_de_flujo'

    nombre = models.CharField(unique=True, max_length=45)
    actividades = []
    def __unicode__(self):
        return self.nombre