from django.urls import include, path
from rest_framework import routers

from core.views import CategoryViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
app_name = 'core'

urlpatterns = [
    path('', include(router.urls))
]