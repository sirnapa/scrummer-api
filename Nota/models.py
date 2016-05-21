from __future__ import unicode_literals
from django.db import models
#from UserStory.models import UserStory



class Nota (models.Model):
    """Clase Nota"""
    class Meta:
        verbose_name = 'nota'
        verbose_name_plural = 'notas'

    texto = models.CharField(max_length=150)
#    userStory = models.ForeignKey(UserStory, null=True, blank=True, default=None)


    def __unicode__(self):
     return self.texto