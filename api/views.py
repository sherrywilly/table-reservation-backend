from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RestSerializer, CategorySerializer, ItemSerializer
from restaurant.models import Restaurant, Category, Item
from rest_framework.response import Response
from api.serializers import SingleRestSerializer
from rest_framework import status
# Create your views here.


class RestApiView(APIView):
    def get(self, request, format=None, pk=None):
        if pk is not None:
            try:

                rest = Restaurant.objects.get(id=pk)
                serializer = SingleRestSerializer(
                    rest, context={'request': request})
                context = {
                    'message': "data fetched successfully",
                    'data': serializer.data
                }
                response_status = status.HTTP_200_OK
            except:
                context = {
                    'message': "invalid primary key"
                }
                response_status = status.HTTP_404_NOT_FOUND
            return Response(context, status=response_status)
        else:

            rest = Restaurant.objects.all()
            serializer = RestSerializer(
                rest, many=True, context={'request': request})
            return Response(serializer.data)


class CategoryApiView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
