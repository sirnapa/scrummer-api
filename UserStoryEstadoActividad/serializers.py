from rest_framework import serializers
from UserStoryEstadoActividad.models import UserStoryEstadoActividad


class UserStoryEstadoActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoryEstadoActividad
        fields = ('userStory','actividad',)
