from django.urls import include, path
from rest_framework import routers

from API.views import HealthViewSet

router =routers.DefaultRouter()
router.register('users',HealthViewSet)

urlpatterns = [
    path ('',include(router.urls))
]