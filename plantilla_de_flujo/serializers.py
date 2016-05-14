from rest_framework import serializers
from rest_framework.reverse import reverse
from actividad.models import actividad
from plantilla_de_flujo.models import plantilla_de_flujo

#actividad= actividad()
class plantilla_de_flujoSerializer(serializers.ModelSerializer):
    #assigned = serializers.SlugRelatedField (
    #    slug_field=actividad.nombre, required=False, read_only=True)
    class Meta:
        model = plantilla_de_flujo
        fields = ('nombre','actividades','id',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('plantilla_de_flujo-detalle',
                            kwargs={'pk': obj.pk}, request=request),
        }