from __future__ import unicode_literals
from rest_framework import permissions
from django.db import models as modelsdb
from django.conf import settings
from permiso.models import permiso
from proyecto.models import proyecto
from django.contrib.auth import models

class rol(modelsdb.Model):

    """Clase rol"""
    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'roles'


    NOMBRE_DESARROLLADOR = 1
    NOMBRE_SCRUM_MASTER = 2
    NOMBRE_ADMINISTRADOR = 3

    NOMBRE_CHOICES =((NOMBRE_DESARROLLADOR,('DESARROLLADOR')),
                  (NOMBRE_SCRUM_MASTER, ('SCRUM_MASTER')),
                  (NOMBRE_ADMINISTRADOR,('ADMINISTRADOR')),
                  )


    proyecto = modelsdb.ForeignKey(proyecto, null=True, blank=True, default=None)
    nombre = modelsdb.SmallIntegerField(choices=NOMBRE_CHOICES, default= NOMBRE_ADMINISTRADOR)
    asignado = modelsdb.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    permisosdelrol= modelsdb.ManyToManyField(models.Permission,verbose_name=('permisosdelrol'),
                                               blank=True,
                                               help_text=('Especifica permisos del rol'),
                                               related_name="rol_set",
                                               related_query_name="user",
                                               )
    def __unicode__(self):
        return self.nombre