from rest_framework import serializers
from restaurant.models import Restaurant


class RestSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description",
                  "address", "status", "categorys", "logo"]
        depth = 2

    def get_logo(self, obj):
        return self.context['request'].build_absolute_uri(obj.logo.url)
