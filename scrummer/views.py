from scrummer.models import usuario
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scrummer_is.serializers import UserSerializer, GroupSerializer, UsuarioSerializer
from scrummer_is.serializers import UserSerializer, GroupSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet,APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.order_by('user')
    serializer_class = UsuarioSerializer