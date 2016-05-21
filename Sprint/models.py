from __future__ import unicode_literals
from django.db import models


# from UserStory.models import UserStory

class Sprint(models.Model):
    """Clase Sprint"""

    class Meta:
        verbose_name = 'sprint'
        verbose_name_plural = 'sprints'


    horas_hombre = models.IntegerField()
    estado = models.CharField(max_length=50, primary_key=False)

    #    userStories = models.ManyToOneRel(UserStory, null=True, blank=True, default=None)
    def __unicode__(self):
        return self.estado
