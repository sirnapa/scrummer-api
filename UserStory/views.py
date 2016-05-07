from rest_framework import viewsets, authentication, permissions
from UserStory.models import UserStory
from UserStory.serializers import UserStorySerializer

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
    queryset = UserStory.objects.order_by('descripcion')
    serializer_class = UserStorySerializer
