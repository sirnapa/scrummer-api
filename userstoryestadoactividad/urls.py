from rest_framework.routers import DefaultRouter

from UserStoryEstadoActividad import views

router = DefaultRouter(trailing_slash=False)
router.register(r'userstoryestadoactividad',views.UserStoryEstadoActividadViewSet)