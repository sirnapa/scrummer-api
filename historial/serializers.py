from rest_framework import serializers
from historial.models import historial


class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = historial
        fields = ('descripcion','fecha',)
