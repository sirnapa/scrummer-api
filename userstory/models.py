from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from sprint.models import sprint
from flujo.models import flujo
from historial.models import historial
from adjunto.models import adjunto
from nota.models import nota
#from enum import Enum

class userstory (models.Model):
    """Clase UserStory"""
    class Meta:
        verbose_name = 'userstory'
        verbose_name_plural = 'userstories'

    PRIORIDAD = (
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    )

    descripcion = models.CharField(max_length=150)
    usuario = models.ForeignKey(User, null=True, blank=True, default=None)
    valornegocio = models.SmallIntegerField(default=0)
    tiempoestimado = models.SmallIntegerField(default=0)
    tiemporeal = models.SmallIntegerField(default=0)
    sprint = models.ForeignKey(sprint, null=True, blank=True, default=None)
    flujo = models.ForeignKey(flujo, null=True, blank=True, default=None)
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD, default=0)
    historial = models.ForeignKey(historial, null=True, blank=True, default=None)
    adjunto = models.ForeignKey(adjunto, null=True, blank=True, default=None)
    def __unicode__(self):
     return self.descripcion
