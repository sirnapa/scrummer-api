from rest_framework import serializers
from UserStory.models import UserStory


class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStory
        fields = ('descripcion', 'usuario', 'valorNegocio', 'tiempoEstimado', 'tiempoReal', 'sprint', 'flujo', 'prioridad',)

