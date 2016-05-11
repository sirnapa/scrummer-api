from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from Sprint.models import Sprint
from flujo.models import flujo
from enum import Enum

class UserStory (models.Model):
    """Clase UserStory"""
    class Meta:
        verbose_name = 'userStory'
        verbose_name_plural = 'userStories'

    PRIORIDAD = (
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    )

    descripcion = models.CharField(max_length=150)
    usuario = models.ForeignKey(User, null=True, blank=True, default=None)
    valorNegocio = models.SmallIntegerField(default=0)
    tiempoEstimado = models.SmallIntegerField(default=0)
    tiempoReal = models.SmallIntegerField(default=0)
    sprint = models.ForeignKey(Sprint, null=True, blank=True, default=None)
    flujo = models.ForeignKey(flujo, null=True, blank=True, default=None)
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD, default=0)

    def __unicode__(self):
     return self.descripcion
