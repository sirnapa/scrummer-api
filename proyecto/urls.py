from rest_framework.routers import DefaultRouter

from proyecto import views

router = DefaultRouter()
router.register(r'proyecto',views.proyectoViewSet)