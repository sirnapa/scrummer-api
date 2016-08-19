from rest_framework import viewsets, authentication, permissions
from sprint.models import sprint
from sprint.serializers import SprintSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



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


class SprintViewSet(viewsets.ModelViewSet):
    queryset = sprint.objects.order_by('estado')
    serializer_class = SprintSerializer

    def get_queryset(self):
        queryset = sprint.objects.all()
        proyecto = self.request.query_params.get('proyecto', None)
        if proyecto is not None:
            queryset = queryset.filter(proyecto=proyecto)
        return queryset