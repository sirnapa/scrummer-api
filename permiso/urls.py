from rest_framework.routers import DefaultRouter

from permiso import views

router = DefaultRouter(trailing_slash=False)
router.register(r'permiso',views.permisoViewSet)