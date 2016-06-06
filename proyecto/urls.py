from rest_framework.routers import DefaultRouter

from proyecto import views

router = DefaultRouter(trailing_slash=False)
router.register(r'proyecto',views.proyectoViewSet)