from rest_framework import serializers
from adjunto.models import adjunto


class AdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = adjunto
        fields = ('nombre','archivo')