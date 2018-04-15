# todos/views.py
from rest_framework import generics

from . import models
from . import serializers


class ListActor(generics.ListCreateAPIView):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer


class DetailActor(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
