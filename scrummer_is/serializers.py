from scrummer.models import usuario
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
        firstname = serializers.CharField(source='user.first_name')
        lastname = serializers.CharField(source='user.last_name')
        estado = serializers.BooleanField(source='user.is_active')
        password = serializers.CharField(source='user.password')

        class Meta:
                model = usuario
                fields = (
                        'id', 'username', 'email', 'firstname', 'lastname','estado','password',
                        'createdat', 'updatedat', 'url',
                )
                read_only_fields = ('createdat', 'updatedat', 'url')

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

                return usuario(user=user, **validated_data)