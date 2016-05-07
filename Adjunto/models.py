from __future__ import unicode_literals
from django.db import models
from UserStory.models import UserStory



class Adjunto (models.Model):
    """Clase Adjunto"""
    class Meta:
        verbose_name = 'adjunto'
        verbose_name_plural = 'adjuntos'

    nombre = models.CharField(max_length=150)
    #archivo
    userStory = models.ForeignKey(UserStory, null=True, blank=True, default=None)


    def __unicode__(self):
     return self.nombre