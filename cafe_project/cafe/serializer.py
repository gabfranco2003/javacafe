from rest_framework import serializers
from .models import MenuItem, CarouselItem, Review

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Use username in the serialized data

    class Meta:
        model = Review
        fields = ['id', 'menu_item', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['created_at']
