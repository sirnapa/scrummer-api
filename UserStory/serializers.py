from rest_framework import serializers
from UserStory.models import UserStory
from Sprint.models import Sprint
from flujo.models import flujo
class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        sprint = serializers.SlugRelatedField(
           slug_field=Sprint.pk, read_only=True)
        flujo = serializers.SlugRelatedField(
            slug_field=flujo.pk, read_only=True)
        model = UserStory
        fields = ('descripcion', 'usuario', 'valorNegocio', 'tiempoEstimado', 'tiempoReal', 'sprint', 'flujo', 'prioridad',
                  'historial','adjunto','nota',)

