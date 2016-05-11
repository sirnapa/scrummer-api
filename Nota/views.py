from rest_framework import viewsets, authentication, permissions
from Nota.models import Nota
from Nota.serializers import NotaSerializer

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


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.order_by('texto')
    serializer_class = NotaSerializer
