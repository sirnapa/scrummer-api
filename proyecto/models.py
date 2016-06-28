from __future__ import unicode_literals

from django.db import models

class proyecto (models.Model):
    """Clase proyecto"""
    class JSONAPIMeta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'

    nombre = models.CharField(unique=True, max_length=45)
    descripcion = models.CharField(max_length=150)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()

    def __unicode__(self):
     return self.nombre