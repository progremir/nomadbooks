from django.urls import include, path
from rest_framework import routers

from core.views import CategoryViewSet, AuthorViewSet, BookViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]
