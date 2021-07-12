
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.settings import APISettings
from restaurant.models import Location, Restaurant, Item, Category
from customer.models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
user = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    auth_token = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = user
        fields = ['id', 'username', 'email', 'password', 'auth_token']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        token, created = Token.objects.get_or_create(
            user_id=user.id)
        x = str(token)
        # try:
        #     context = {
        #         'id': user.id,
        #         'username': user.username,
        #         'email': user.email,
        #         'Token': x
        #     }
        # except Exception as KeyError:
        #     context = user
        # print(context)
        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')


class RestSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description",
                  "address", "status", "categorys", "logo"]
        depth = 2

    def get_logo(self, obj):
        return self.context['request'].build_absolute_uri(obj.logo.url)


class SingleRestSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        # fields = "__all__"
        depth = 2
        exclude = ['categorys', 'user']

    def get_logo(self, obj):
        return self.context['request'].build_absolute_uri(obj.logo.url)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "price"]


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "shop", "items"]
        # depth = 2


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingItem
        fields = ['id', 'food', 'quantity']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'restaurant', 'user', 'order_status',
                  'guest', 'date', 'time', 'created_at', 'order_items']
        # depth = 1
