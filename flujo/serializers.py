from rest_framework import serializers
from rest_framework.reverse import reverse
from actividad.models import actividad
from flujo.models import flujo
#actividad= actividad()
class flujoSerializer(serializers.ModelSerializer):
    #actividades = serializers.SlugRelatedField (
    #     slug_field=actividad.nombre, required=False, read_only=True)

    class Meta:
        model = flujo
        fields = ('nombre',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('flujo-detalle',
                            kwargs={'pk': obj.pk}, request=request),
        }