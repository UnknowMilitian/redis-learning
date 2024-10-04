from django.shortcuts import render
from rest_framework import generics, permissions

# Project imports
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

# Redis imports
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# Create your views here.
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(60 * 5))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @method_decorator(cache_page(60 * 5))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
