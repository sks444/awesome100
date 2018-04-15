from rest_framework import serializers
from . import models


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = '__all__'
