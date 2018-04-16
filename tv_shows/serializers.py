from rest_framework import serializers
from . import models


class TvShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TvShow
        fields = '__all__'
