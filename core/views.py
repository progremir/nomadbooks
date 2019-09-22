from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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

    @action(detail=True, methods=['post'], permission_classes=(IsAuthenticated,), url_path='mark_as_read')
    def mark_as_read(self, request, pk=None):
        book = self.get_object()
        book.read_by.add(request.user)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=(IsAuthenticated,), url_path='read_list')
    def read_list(self, request, pk=None):
        books = Book.objects.filter(read_by=request.user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class ReviewViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
