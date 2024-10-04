from django.shortcuts import render
from rest_framework import generics, permissions

from rest_framework.views import APIView
from rest_framework.response import Response

# Project imports
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

# Redis imports
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator


# Create your views here.
class CategoryAPIView(APIView):
    def get(self, request):

        categories = cache.get("categories")

        if not categories:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            cache.set("categories", serializer.data, timeout=60 * 5)
        else:
            serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete("categories")
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()

            cache.delete("categories")
            return Response(status=204)
        except Category.DoesNotExist:
            return Response(status=404)


class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @method_decorator(cache_page(60 * 5))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
