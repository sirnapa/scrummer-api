from rest_framework import serializers
from rest_framework.reverse import reverse
from proyecto.models import  proyecto

class proyectoSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = proyecto
        fields = ('nombre','descripcion','fechaInicio','fechaFin')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('proyecto-detalle',
                            kwargs={'pk': obj.pk}, request=request),
        }