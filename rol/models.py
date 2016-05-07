from __future__ import unicode_literals

from django.db import models
from permiso.models import permiso
from proyecto.models import proyecto

class rol(models.Model):

     """Clase rol"""

     class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'roles'

     nombre = models.CharField(unique=True, max_length=45)
     permisos = models.ManyToManyField('permiso.permiso', blank=True, default=None)
     proyecto = models.ForeignKey(proyecto, null=True, blank=True, default=None)

     def __unicode__(self):
         return self.nombre