from rest_framework import serializers
from userstoryestadoactividad.models import userstoryestadoactividad


class UserStoryEstadoActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = userstoryestadoactividad
        fields = ('userStory','actividad','estado',)