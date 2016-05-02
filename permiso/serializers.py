from rest_framework import serializers
from rest_framework.reverse import reverse
from permiso.models import permiso

class permisoSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')

    class Meta:
        model = permiso
        fields = ('nombre')

    def get_links(self,obj):
        request= self.context['request']
        return {
            'self': reverse('permiso-detalle',
                            kwargs={'pk': obj.pk},request=request),
        }
