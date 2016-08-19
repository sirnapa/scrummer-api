from rest_framework import serializers
from userstory.models import userstory
from sprint.models import sprint
from flujo.models import flujo
class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        sprint = serializers.SlugRelatedField(
           slug_field=sprint.pk, read_only=True)
        flujo = serializers.SlugRelatedField(
            slug_field=flujo.pk, read_only=True)
        model = userstory
        fields = ('descripcion', 'usuario', 'valornegocio', 'tiempoestimado', 'tiemporeal', 'sprint', 'flujo','proyecto', 'prioridad',
                  'historial','adjunto',)

