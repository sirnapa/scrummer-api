from django.shortcuts import render

from rest_framework import viewsets, authentication, permissions
from actividad.models import actividad
from actividad.serializers import actividadSerializer

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
class actividadViewSet(viewsets.ModelViewSet):
    queryset = actividad.objects.order_by('nombre')
    serializer_class = actividadSerializer
