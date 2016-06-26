from rest_framework.routers import DefaultRouter

from plantilladeflujo import views

router = DefaultRouter(trailing_slash=False)
router.register(r'plantilladeflujo', views.PlantillaDeFlujoViewSet)