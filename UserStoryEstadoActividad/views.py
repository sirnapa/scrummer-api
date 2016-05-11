from rest_framework import viewsets, authentication, permissions
from UserStoryEstadoActividad.models import UserStoryEstadoActividad
from UserStoryEstadoActividad.serializers import UserStoryEstadoActividadSerializer

class DefaultsMixin(object):
    """Configuracion por defecto para la autenticacion, permisos, filtrado y paginacion de la view"""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permissions_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class UserStoryEstadoActividadViewSet(viewsets.ModelViewSet):
    queryset = UserStoryEstadoActividad.objects.order_by('actividad')
    serializer_class = UserStoryEstadoActividadSerializer