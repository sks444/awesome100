from rest_framework import serializers
from . import models


class ComedianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comedian
        fields = '__all__'
