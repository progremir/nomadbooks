from django.urls import include, path
from rest_framework import routers

from core.views import CategoryViewSet, AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
