from rest_framework.routers import DefaultRouter

from plantilla_de_flujo import views

router = DefaultRouter()
router.register(r'plantilla_de_flujo',views.plantilla_de_flujoViewSet)