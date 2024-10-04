from django.urls import path
from .views import CategoryListAPIView, ItemListAPIView

urlpatterns = [
    path("category-list", CategoryListAPIView.as_view(), name="category-list"),
    path("item-list", ItemListAPIView.as_view(), name="item-list"),
]
