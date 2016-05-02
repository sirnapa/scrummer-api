from rest_framework import serializers
from rest_framework.reverse import reverse
from rol.models import rol
from proyecto.models import proyecto

proyect= proyecto()
class rolSerializer(serializers.ModelSerializer):
    assigned = serializers.SlugRelatedField (
        slug_field=proyect.nombre, required=False, read_only=True)
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = rol
        fields = ('nombre','permiso','proyecto')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('rol-detalle',
                            kwargs={'pk': obj.pk}, request=request),
        }
