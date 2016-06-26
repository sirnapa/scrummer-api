from __future__ import unicode_literals

from django.db import models


from django.contrib import admin

class plantilladeflujo (models.Model):
    """Clase Plantilla de flujo"""

    class Meta:
        verbose_name = 'plantillaDeFlujo'
        verbose_name_plural = 'plantillaDeFlujos'

    nombre = models.CharField(unique=True, max_length=45)
    actividades = models.CharField(null=True, max_length=500)

    #def setactividades(self, x):
    #    self.actividades = json.dumps(x)

    #def getactividades(self, x):
    #    return json.loads(self.actividades)






def __unicode__(self):
 return self.nombre