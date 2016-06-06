from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions
from flujo.models import flujo
from flujo.serializers import flujoSerializer



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




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
class flujoViewSet(viewsets.ModelViewSet):
    queryset = flujo.objects.order_by('nombre')
    serializer_class = flujoSerializer

