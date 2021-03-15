from rest_framework import serializers
from restaurant.models import Restaurant, Item, Category


class RestSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description",
                  "address", "status", "categorys", "logo"]
        depth = 2

    def get_logo(self, obj):
        return self.context['request'].build_absolute_uri(obj.logo.url)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "price"]


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "shop", "items"]