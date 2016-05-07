from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

#Import de los modulos

from permiso import views as viewsPermiso
from proyecto import views as viewsProyecto
from rol import views as viewsRol
from UserStory import views as viewsUserStory
from Sprint import views as viewsSprint
from scrummer import views
from actividad import views as viewsActividad
from flujo import views as viewsFlujo
from plantilla_de_flujo import views as viewsPlantilla_de_Flujo

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permisos', viewsPermiso.permisoViewSet)
router.register(r'proyectos', viewsProyecto.proyectoViewSet)
router.register(r'roles',viewsRol.rolViewSet)
router.register(r'userStories', viewsUserStory.UserStoryViewSet)
router.register(r'sprints', viewsSprint.SprintViewSet)
router.register(r'actividad', viewsActividad.actividadViewSet)
router.register(r'flujo', viewsFlujo.flujoViewSet)
router.register(r'plantilla_de_flujo',viewsPlantilla_de_Flujo.plantilla_de_flujoViewSet)
# Wire up our API using automatic URL routing...
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token, name='api-token'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]