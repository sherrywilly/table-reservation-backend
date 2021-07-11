from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets
import json
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LocationSerializer, RestSerializer, CategorySerializer, ItemSerializer, UserSerializer
from restaurant.models import Location, Restaurant, Category, Item
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


class RestWithLocation(APIView):
    def get(self, request, pk, format=None):
        if pk is not None:
            rest = Restaurant.objects.filter(location_id=pk)
        else:
            rest = Restaurant.objects.all()
        if rest.count == 0:
            return Response(status=404)
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


class LocationApiView(APIView):
    def get(self, request):
        loc = Location.objects.all()
        serialiser = LocationSerializer(loc, many=True)
        return Response(serialiser.data)


#! ############################### user model ##############################

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False, is_superuser=False)
    serializer_class = UserSerializer
