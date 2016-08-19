from rest_framework import viewsets, authentication, permissions
from userstory.models import userstory
from userstory.serializers import UserStorySerializer

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


class UserStoryViewSet(viewsets.ModelViewSet):
    queryset = userstory.objects.order_by('descripcion')
    serializer_class = UserStorySerializer

    def get_queryset(self):
        queryset = userstory.objects.all()
        proyecto = self.request.query_params.get('proyecto', None)
        if proyecto is not None:
            queryset = queryset.filter(proyecto=proyecto)
        return queryset