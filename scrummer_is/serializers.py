from scrummer.models import Usuario
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UsuarioSerializer(serializers.ModelSerializer):

        id = serializers.IntegerField(source='pk', read_only=True)
        username = serializers.CharField(source='user.username', required=True)
        email = serializers.CharField(source='user.email')
        first_name = serializers.CharField(source='user.first_name')
        last_name = serializers.CharField(source='user.last_name')

        class Meta:
                model = Usuario
                fields = (
                        'id', 'username', 'email', 'first_name', 'last_name',
                        'created_at', 'updated_at', 'url', 'nombre', 'apellido', 'direccion', 'telefono', 'observacion', 'estado',
                )
                read_only_fields = ('created_at', 'updated_at', 'url')

        def update(self, instance, validated_data):
                # First, update the User
                user_data = validated_data.pop('user', None)
                for attr, value in user_data.items():
                        setattr(instance.user, attr, value)
                instance.user.save()
                # Then, update Usuario
                for attr, value in validated_data.items():
                        setattr(instance, attr, value)
                instance.save()
                return instance

        def create(self, validated_data):

                user_data = validated_data.pop('user')
                user = User.objects.create(**user_data)

                return Usuario(user=user, **validated_data)