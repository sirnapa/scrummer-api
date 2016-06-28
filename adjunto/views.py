from rest_framework import viewsets, authentication, permissions
from adjunto.models import adjunto
from adjunto.serializers import AdjuntoSerializer

class DefaultsMixin(object):
    """Configuracion por defecto para la autenticacion, permisos, filtrado y paginacion de la view"""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permissions_classes = (
        permissions.IsAuthenticated, permissions.DjangoModelPermissions,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class AdjuntoViewSet(viewsets.ModelViewSet):
    queryset = adjunto.objects.order_by('nombre')
    serializer_class = AdjuntoSerializer