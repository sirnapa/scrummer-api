from rest_framework import serializers
from rest_framework.reverse import reverse
from rol.models import rol
from proyecto.models import proyecto
from django.contrib.auth.models import AbstractUser

proyect= proyecto()
class rolSerializer(serializers.ModelSerializer):
   # assigned = serializers.SlugRelatedField (
        #slug_field=proyect.nombre, required=False, read_only=True)
    #links = serializers.SerializerMethodField('get_links')
    #rol_display =serializers.SerializerMethodField('get_rol_display')
    #nombre_rol_display =serializers.SerializerMethodField('get_nombre_rol_display')
    #permisos_display = serializers.SerializerMethodField('get_status_display')
    class Meta:
        model = rol
        fields = ('nombre','permisos_del_rol','proyecto',)


    def get_nombre_rol_display(self, obj):
        return obj.get_nombre_rol_display()




    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('rol-detalle',
                            kwargs={'pk': obj.pk}, request=request),
        }
