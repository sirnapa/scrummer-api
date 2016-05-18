from rest_framework.routers import DefaultRouter

from UserStory import views

router = DefaultRouter(trailing_slash=False)
router.register(r'userStory',views.UserStoryViewSet)