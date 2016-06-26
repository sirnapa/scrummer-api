from __future__ import unicode_literals
from django.db import models
from userstory.models import userstory
from actividad.models import actividad
from django.contrib import admin


class userstoryestadoactividad (models.Model):
    """Clase Nota"""
    class Meta:
        verbose_name = 'userStoryEstadoActividad'
        verbose_name_plural = 'userStoryEstadoActividades'

    ESTADO = (
        ('0', 'TO DO'),
        ('1', 'DOING'),
        ('2', 'DONE'),
    )

    userStory = models.ForeignKey(userstory, null=True, blank=True, default=None)
    actividad = models.ForeignKey(actividad, null=True, blank=True, default=None)
    estado = models.CharField(max_length=1, choices=ESTADO, default=0)



def __unicode__(self):
 return self.actividad