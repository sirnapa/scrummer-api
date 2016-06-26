from rest_framework import serializers
from plantilladeflujo.models import plantilladeflujo


class PlantillaDeFlujoSerializer(serializers.ModelSerializer):

    class Meta:
        model = plantilladeflujo
        fields = ('nombre','actividades','id',)
