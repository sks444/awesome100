# todos/views.py
from rest_framework import generics

from . import models
from . import serializers


class ListDirector(generics.ListCreateAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer


class DetailDirector(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
