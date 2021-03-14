from django.urls import path
from .api_views import *

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('profiles/', ProfileListAPIView.as_view(), name='profiles'),
    path('products/<int:pk>/detail/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('products/create/', ProductCreate.as_view(), name='company_create'),
]

