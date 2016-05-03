from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from permiso.urls import router
from proyecto.urls import router
from rol.urls import router

from permiso import views as viewsPermiso
from proyecto import views as viewsProyecto
from rol import views as viewsRol
from scrummer import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permisos', viewsPermiso.permisoViewSet)
router.register(r'proyectos', viewsProyecto.proyectoViewSet)
router.register(r'roles',viewsRol.rolViewSet)
# Wire up our API using automatic URL routing...
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token, name='api-token'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]