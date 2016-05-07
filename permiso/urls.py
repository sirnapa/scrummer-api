from rest_framework.routers import DefaultRouter

from permiso import views

router = DefaultRouter()
router.register(r'permiso',views.permisoViewSet)