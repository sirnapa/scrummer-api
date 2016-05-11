from __future__ import unicode_literals
from django.db import models
from UserStory.models import UserStory
from actividad.models import actividad



class UserStoryEstadoActividad (models.Model):
    """Clase Nota"""
    class Meta:
        verbose_name = 'userStoryEstadoActividad'
        verbose_name_plural = 'userStoryEstadoActividades'

    #estado
    userStory = models.ForeignKey(UserStory, null=True, blank=True, default=None)
    actividad = models.ForeignKey(actividad, null=True, blank=True, default=None)


    def __unicode__(self):
     return self.actividad
