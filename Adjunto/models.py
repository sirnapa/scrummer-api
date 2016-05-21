from __future__ import unicode_literals
from django.db import models
#from UserStory.models import UserStory
from django.contrib.auth.models import User


class Adjunto (models.Model):
    """Clase Adjunto"""
    class Meta:
        verbose_name = 'adjunto'
        verbose_name_plural = 'adjuntos'
        #app_label = 'permission'

    nombre = models.CharField(max_length=150)
    archivo = models.FileField(null=True,blank=True)
#    userStory = models.ForeignKey(UserStory, null=True, blank=True, default=None)


    def __unicode__(self):
     return self.nombre

#from permission import add_permission_logic
#from permission.logics import AuthorPermissionLogic
#add_permission_logic(Adjunto, AuthorPermissionLogic())