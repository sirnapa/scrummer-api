from __future__ import unicode_literals
from django.db import models


class Sprint (models.Model):
    """Clase Sprint"""
    class Meta:
        verbose_name = 'sprint'
        verbose_name_plural = 'sprints'



    estado = models.CharField(max_length=50)
    def __unicode__(self):
     return self.estado
