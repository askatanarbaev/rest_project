from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
from .serializers import (ProductSerializer, ProfileSerializer,
                          ProductDetailSerializer, ProductUpdateSerializer,
                          )
from ..models import Product, Profile
from .pagination import ListPagination
from django.contrib.auth.models import User
from rest_framework import permissions
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', 'category')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProfileListAPIView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('first_name',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


# class for register user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

