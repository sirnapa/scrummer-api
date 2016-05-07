from rest_framework import serializers
from rest_framework.reverse import reverse
from actividad.models import  actividad

class actividadSerializer(serializers.ModelSerializer):

    class Meta:
        model = actividad
        fields = ('nombre','orden','flujo',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('actividad-detalle',
                            kwargs={'pk': obj.pk}, request=request),
        }