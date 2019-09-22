from django.urls import include, path
from rest_framework import routers

from core.views import CategoryViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
