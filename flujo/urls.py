from rest_framework.routers import DefaultRouter

from flujo import views

router = DefaultRouter(trailing_slash=False)
router.register(r'flujo',views.flujoViewSet)