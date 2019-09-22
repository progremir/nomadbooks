from rest_framework import serializers

from .models import Category, Author, Book, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'rating', 'review', 'user', 'book')


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'authors')


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    authors = AuthorSerializer(many=True)
    read_by = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'authors', 'reviews', 'read_by')
