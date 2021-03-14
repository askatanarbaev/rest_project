from rest_framework import serializers
from ..models import *
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


# serializers class for users
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


# serializer class  for detail
class ProductDetailSerializer(serializers.ModelSerializer):

    created_by = UserSerializer()

    class Meta:
        model = Product
        fields = '__all__'


# serializer class for update
class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


