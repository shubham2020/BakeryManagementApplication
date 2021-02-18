from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.db.models import Count
from django.contrib.auth.models import User
from account.api.serializers import UserSerializer, RegistrationSerializer
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from account.models import Orders, OrderedItems
from bakery.models import BakeryItems
from bakery.api.serializers import UserProductListSerializer
from account.api.serializers import (
    OrdersSerializer, 
    OrderHistorySerializer, 
    BillSerializer,
    PreBillSerializer
)

@api_view(['PUT',])
def registration(request):
    if request.method == 'PUT':
        try:
            user = request.data
            serializer = RegistrationSerializer(data=user)
            if serializer.is_valid():
                user = serializer.save()
                token = Token.objects.get(user=user).key
                return Response(data={"token": token}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Error :", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

# Using rest_framework view for login handling

@api_view(['GET',])
def get_product_list(request):

    if request.method == 'GET':
        try:
            items = BakeryItems.objects.all()
            serializer = UserProductListSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def place_order(request):

    if request.method == 'PUT':
        try:
            user = request.user
            order = request.data
            order['user'] = user.id
            serializer = OrdersSerializer(data=order)

            if serializer.is_valid():
                serializer.save()
                return Response({"response": "Order successfull placed"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)

        except Exception as e:
            return Response(status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def get_order_history(request):

    if request.method == 'GET':
        try:
            user = request.user
            order_history = Orders.objects.filter(user=user)
            serializer = OrderHistorySerializer(order_history, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def get_bill(request, id):

    if request.method == 'GET':
        try:
            user = request.user
            order = Orders.objects.filter(user=user).get(pk=id)
            preser = PreBillSerializer(order.ordereditems_set, many=True)
            total = 0
            for items in preser.data:
                print(items)
                total += items['price']
            serializer = BillSerializer(order).data
            serializer["purchased_items"] = preser.data
            serializer["total_price"] = total
            print(serializer)
            return Response(serializer, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
@permission_classes((IsAdminUser,))
def hottest_selling_item(request):

    if request.method == 'GET':
        try:
            count_list = OrderedItems.objects.values('item').order_by('item').annotate(count=Count('item'))
            max = 0
            for i, val in enumerate(count_list):
                if val['count'] > max:
                    max = val['count']

            hottest_selling_items = []
            for i, val in enumerate(count_list):
                if val['count'] == max:
                    hottest_selling_items.append(BakeryItems.objects.get(pk=val['item']))

            print(hottest_selling_items)

            serializer = UserProductListSerializer(hottest_selling_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)





