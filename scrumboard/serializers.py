from rest_framework import serializers
from .models import Card, List


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
