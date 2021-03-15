from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RestSerializer, CategorySerializer, ItemSerializer
from restaurant.models import Restaurant, Category, Item
from rest_framework.response import Response
# Create your views here.


class RestApiView(APIView):
    def get(self, request, format=None):
        rest = Restaurant.objects.all()
        serializer = RestSerializer(
            rest, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryApiView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
