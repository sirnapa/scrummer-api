from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions
from plantilla_de_flujo.models import plantilla_de_flujo
from plantilla_de_flujo.serializers import plantilla_de_flujoSerializer

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
class plantilla_de_flujoViewSet(viewsets.ModelViewSet):
    queryset = plantilla_de_flujo.objects.order_by('nombre')
    serializer_class = plantilla_de_flujoSerializer
