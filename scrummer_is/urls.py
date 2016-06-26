from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

#para permisos
from django.conf.urls import patterns
from django.contrib import admin
#########


#Import de los modulos

from permiso import views as viewsPermiso
from proyecto import views as viewsProyecto
from rol import views as viewsRol
from userstory import views as viewsUserStory
#from usuario import views as viewsUsuario
from Sprint import views as viewsSprint
from scrummer import views
from actividad import views as viewsActividad
from flujo import views as viewsFlujo
from Nota import views as viewsNota
from Historial import views as viewsHistorial
from Adjunto import views as viewsAdjunto
from userstoryestadoactividad import views as viewsUserStoryEstadoActividad
from plantilladeflujo import views as viewsPlantillaDeFlujo

import permission; permission.autodiscover()

router = DefaultRouter(trailing_slash=False)


router.register(r'users', views.UserViewSet)
#router.register(r'usuarios',viewsUsuario.UsuarioViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permisos', viewsPermiso.permisoViewSet)
router.register(r'proyectos', viewsProyecto.proyectoViewSet)
router.register(r'roles',viewsRol.rolViewSet)
router.register(r'userstorys', viewsUserStory.UserStoryViewSet)
router.register(r'sprints', viewsSprint.SprintViewSet)
router.register(r'actividades', viewsActividad.actividadViewSet)
router.register(r'flujos', viewsFlujo.flujoViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'notas', viewsNota.NotaViewSet)
router.register(r'historiales', viewsHistorial.HistorialViewSet)
router.register(r'adjuntos',viewsAdjunto.AdjuntoViewSet)
router.register(r'userstoryestadoactividads', viewsUserStoryEstadoActividad.UserStoryEstadoActividadViewSet)
router.register(r'plantilladeflujos', viewsPlantillaDeFlujo.PlantillaDeFlujoViewSet)
# Wire up our API using automatic URL routing...
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^login/', obtain_auth_token),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]