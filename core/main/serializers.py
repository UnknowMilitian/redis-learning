from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["category", "title", "description"]
