from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions
from permiso.models import permiso
from permiso.serializers import permisoSerializer

class DefaultsMixin(object):
    """Configuracion por defecto para la autenticacion, permisos, filtrado y paginacion de la view"""

    authentication_classes =(
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permissions_classes = (
         permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
class permisoViewSet(viewsets.ModelViewSet):
    queryset = permiso.objects.order_by('nombre')
    serializer_class = permisoSerializer
