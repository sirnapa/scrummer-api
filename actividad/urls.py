from rest_framework.routers import DefaultRouter

from actividad import views

router = DefaultRouter()
router.register(r'actividad',views.actividadViewSet)