from rest_framework import serializers

from books.models import Book
# Create your class here.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")