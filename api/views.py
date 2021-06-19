import json
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RestSerializer, CategorySerializer, ItemSerializer
from restaurant.models import Restaurant, Category, Item
from rest_framework.response import Response
from api.serializers import OrderSerializer, SingleRestSerializer
from rest_framework import status
from customer.models import Booking, BookingItem
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
    def get(self, request, format=None, pk=None):
        category = Category.objects.filter(shop_id=pk)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class OrderApiView(APIView):
    def get(self, request, format=None):
        order = Booking.objects.get(id="ef373175-8752-4018-ac12-487b89538ff1")
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data.get('data'))
        xx = json.loads(request.data['data'])
        print(type(xx))
        serializer = OrderSerializer(data=xx)
        if serializer.is_valid():
            x = serializer.save()
            for i in xx['order_items']:
                print(i)
                count = i['quantity']
                fo_id = i['food']['id']
                print(fo_id)
                BookingItem.objects.create(
                    order_id=x.id, food_id=fo_id, quantity=count)
        else:
            print(serializer.errors)
        return Response(serializer.data)
