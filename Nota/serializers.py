from rest_framework import serializers
from Nota.models import Nota


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ('texto',)
