from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from scrummer import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing...
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]