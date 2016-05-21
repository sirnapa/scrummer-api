from rest_framework import serializers
from UserStory.models import UserStory
from Sprint.models import Sprint

class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        sprint = serializers.SlugRelatedField(
           slug_field=Sprint.pk, read_only=True)

        model = UserStory
        fields = ('descripcion', 'usuario', 'valorNegocio', 'tiempoEstimado', 'tiempoReal', 'sprint', 'flujo', 'prioridad',
                  'historial','adjunto','nota',)

