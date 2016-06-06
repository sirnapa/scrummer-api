from rest_framework import serializers
from Adjunto.models import Adjunto


class AdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjunto
        fields = ('nombre','archivo')