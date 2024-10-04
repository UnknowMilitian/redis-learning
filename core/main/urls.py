from django.urls import path
from .views import CategoryAPIView, ItemListAPIView

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name="category-list"),
    path("item-list", ItemListAPIView.as_view(), name="item-list"),
]
