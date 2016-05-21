from __future__ import unicode_literals
from django.db import models
#from UserStory.models import UserStory



class Historial (models.Model):
    """Clase Historial"""
    class Meta:
        verbose_name = 'historial'
        verbose_name_plural = 'historiales'

    descripcion = models.CharField(max_length=150)
    fecha = models.DateField()
#    userStory = models.ForeignKey(UserStory, null=True, blank=True, default=None)


    def __unicode__(self):
     return self.descripcion