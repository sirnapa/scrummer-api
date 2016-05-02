from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from permiso.urls import router
from proyecto.urls import router
from rol.urls import router

from scrummer import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing...
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token, name='api-token'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]