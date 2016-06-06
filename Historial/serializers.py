from rest_framework import serializers
from Historial.models import Historial


class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = ('descripcion','fecha',)
