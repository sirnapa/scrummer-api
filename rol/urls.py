from rest_framework.routers import DefaultRouter

from rol import views

router = DefaultRouter()
router.register(r'rol',views.rolViewSet)