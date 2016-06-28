from rest_framework import serializers
from nota.models import nota


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = nota
        fields = ('texto',)
