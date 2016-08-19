from __future__ import unicode_literals
from django.db import models
from proyecto.models import proyecto


# from UserStory.models import UserStory

class sprint(models.Model):
    """Clase Sprint"""

    class Meta:
        verbose_name = 'sprint'
        verbose_name_plural = 'sprints'


    horashombre = models.IntegerField(default=0)
    estado = models.CharField(max_length=50, primary_key=False)
    proyecto = models.ForeignKey(proyecto, null=True, blank=True, default=None)

    #    userStories = models.ManyToOneRel(UserStory, null=True, blank=True, default=None)
    def __unicode__(self):
        return self.estado
