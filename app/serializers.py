from rest_framework import serializers
from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        exclude = ['id']
        