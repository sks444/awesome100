# todos/views.py
from rest_framework import generics

from . import models
from . import serializers


class ListComedian(generics.ListCreateAPIView):
    queryset = models.Comedian.objects.all()
    serializer_class = serializers.ComedianSerializer


class DetailComedian(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comedian.objects.all()
    serializer_class = serializers.ComedianSerializer
