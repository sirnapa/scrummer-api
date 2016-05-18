from __future__ import unicode_literals

from django.db import models
import json

class plantilla_de_flujo (models.Model):
    """Clase Plantilla de flujo"""

    class Meta:
        verbose_name = 'plantilla_de_flujo'
        verbose_name_plural = 'plantillas_de_flujo'

    nombre = models.CharField(unique=True, max_length=45)

    actividades = models.CharField(null=True, max_length=500)

    #def setactividades(self, x):
    #    self.actividades = json.dumps(x)

    #def getactividades(self, x):
    #    return json.loads(self.actividades)


    def __unicode__(self):
        return self.nombre