from rest_framework.routers import DefaultRouter

from Adjunto import views

router = DefaultRouter(trailing_slash=False)
router.register(r'adjunto',views.AdjuntoViewSet)