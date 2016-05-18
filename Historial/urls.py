from rest_framework.routers import DefaultRouter

from Historial import views

router = DefaultRouter(trailing_slash=False)
router.register(r'historial',views.HistorialViewSet)