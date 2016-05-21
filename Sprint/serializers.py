from rest_framework import serializers
from Sprint.models import Sprint


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ('id','estado','horas_hombre',)