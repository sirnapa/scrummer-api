from rest_framework.routers import DefaultRouter

from actividad import views

router = DefaultRouter(trailing_slash=False)
router.register(r'actividad',views.actividadViewSet)