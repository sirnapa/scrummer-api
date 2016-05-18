from rest_framework.routers import DefaultRouter

from Sprint import views

router = DefaultRouter(trailing_slash=False)
router.register(r'sprint',views.SprintViewSet)