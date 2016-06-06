from rest_framework import serializers
from rol.models import rol
from scrummer.models import User
from rest_framework.reverse import reverse
class rolSerializer(serializers.ModelSerializer):
    asignado = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False, read_only=True)
    nombre_display = serializers.SerializerMethodField()
    #links=serializers.SerializerMethodField()
    class Meta:
        model = rol
        fields = ( 'nombre','nombre_display','permisos_del_rol','asignado', 'proyecto')

    def get_nombre_display(self,obj):
        return obj.get_nombre_display()

   # def get_links(self,obj):
    #    request = self.context['request']
     #   return {
      #      'self': reverse('rol-detalle', kwargs={'pk': obj.pk}, request=request),
       # }