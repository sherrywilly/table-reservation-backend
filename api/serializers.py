
from django.db.models import fields
from rest_framework import serializers
from rest_framework.settings import APISettings
from restaurant.models import Location, Restaurant, Item, Category
from customer.models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
user = get_user_model()


token = serializers.SerializerMethodField()


# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fields = ['Key']


class UserSerializer(serializers.ModelSerializer):
    # key = TokenSerializer(read_only=True)

    class Meta:
        model = user
        fields = ['id', 'username', 'email', 'password', ]
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(
            user_id=response.id)
        # x = str(token)
        # try:
        #     context = {
        #         'id': response.id,
        #         'username': response.username,
        #         'email': response.email,
        #         'token': x
        #     }
        # except Exception as KeyError:
        #     context = response
        # print(context)
        return response


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
