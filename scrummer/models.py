from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from rol.models import rol
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

# Create your models here.


class usuario(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='usuario')
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=False)
    direccion = models.CharField(max_length=150, null=True)
    telefono = models.CharField(max_length=150, null=True)
    observacion = models.CharField(max_length=150, null=True)
    rol = models.ForeignKey(rol, null=True, blank=True, default=None)

    def __unicode__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            usuario.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        if instance:
            user_profile = usuario.objects.get(user=instance)
            user_profile.delete()