from django.shortcuts import render
from rest_framework import generics, permissions

from rest_framework.views import APIView
from rest_framework.response import Response

# Project imports
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

# Redis imports
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# Create your views here.
class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @method_decorator(cache_page(60 * 5))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
