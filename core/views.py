from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet


from common.permissions import IsAdminUserOrReadOnly
from .models import Category, Author, Book, Review
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer, BookCreateSerializer, ReviewSerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return BookCreateSerializer
        return BookSerializer


class ReviewViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
