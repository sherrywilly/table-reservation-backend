from rest_framework import serializers
from restaurant.models import Restaurant, Item, Category
from customer.models import *


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
