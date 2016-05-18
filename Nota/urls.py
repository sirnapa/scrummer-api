from rest_framework.routers import DefaultRouter

from Nota import views

router = DefaultRouter(trailing_slash=False)
router.register(r'nota',views.NotaViewSet)