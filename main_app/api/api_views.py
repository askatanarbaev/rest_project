from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsOwnerOrReadOnly
from .serializers import (ProductSerializer, ProfileSerializer,
                          ProductDetailSerializer, ProductUpdateSerializer,
                          )
from ..models import Product, Profile
from .pagination import ListPagination
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_context(self):
        context = super(ProductCreate, self).get_serializer_context()
        context.update({
            'created_by': self.request.user
        })
        return context


# class for register user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


