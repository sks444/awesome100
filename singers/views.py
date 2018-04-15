# todos/views.py
from rest_framework import generics

from . import models
from . import serializers


class ListSinger(generics.ListCreateAPIView):
    queryset = models.Singer.objects.all()
    serializer_class = serializers.SingerSerializer


class DetailSinger(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Singer.objects.all()
    serializer_class = serializers.SingerSerializer
