from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from Sprint.models import Sprint


class UserStory (models.Model):
    """Clase UserStory"""
    class Meta:
        verbose_name = 'userStory'
        verbose_name_plural = 'userStories'

    descripcion = models.CharField(max_length=150)
    usuario = models.ForeignKey(User, null=True, blank=True, default=None)
    valorNegocio = models.SmallIntegerField(default=0)
    tiempoEstimado = models.SmallIntegerField(default=0)
    tiempoReal = models.SmallIntegerField(default=0)
    sprint = models.ForeignKey(Sprint, null=True, blank=True, default=None)
    #historial
    #adjunto
    #prioridad
    #nota
    #flujo
    #sprint

    def __unicode__(self):
     return self.descripcion
