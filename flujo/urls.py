from rest_framework.routers import DefaultRouter

from flujo import views

router = DefaultRouter()
router.register(r'flujo',views.flujoViewSet)