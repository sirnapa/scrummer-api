from rest_framework.routers import DefaultRouter

from userstory import views

router = DefaultRouter(trailing_slash=False)
router.register(r'userstory',views.UserStoryViewSet)