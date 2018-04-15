# todos/views.py
from rest_framework import generics

from . import models
from . import serializers


class ListAuthor(generics.ListCreateAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class DetailAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
