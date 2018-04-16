# todos/views.py
from rest_framework import generics

from . import models
from . import serializers


class ListTvShow(generics.ListCreateAPIView):
    queryset = models.TvShow.objects.all()
    serializer_class = serializers.TvShowSerializer


class DetailTvShow(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TvShow.objects.all()
    serializer_class = serializers.TvShowSerializer
