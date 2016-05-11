from rest_framework import viewsets, authentication, permissions
from Historial.models import Historial
from Historial.serializers import HistorialSerializer

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


class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.order_by('fecha')
    serializer_class = HistorialSerializer