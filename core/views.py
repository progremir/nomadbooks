from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from common.permissions import IsAdminUserOrReadOnly
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
