from rest_framework import serializers
from . import models


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Singer
        fields = '__all__'
