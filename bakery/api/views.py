from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bakery.models import (
    Ingredients, 
    BakeryItems, 
    Composition, 
    RawMaterials, 
    EndProducts
    )
from bakery.api.serializers import (
    IngredientsSerializer, 
    BakeryItemsSerializer, 
    CompositionSerializer,
    RawMaterialsSerializer,
    EndProductsSerializer
    )

@api_view(['GET',])
@permission_classes((IsAdminUser,))
def get_bakery_item(request, id):

    if request.method == 'GET':
        try:
            item = BakeryItems.objects.get(pk=id)
            serializer = BakeryItemsSerializer(item)
            return Response(serializer.data)

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT',])
@permission_classes((IsAdminUser,))
def add_bakery_item(request):

    if request.method == 'PUT':
        try:
            bakeryItem = BakeryItemsSerializer(data=request.data)
            if bakeryItem.is_valid():
                bakeryItem.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                print(bakeryItem.errors)

        except Exception as e:
            print("Error : ", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT',])
@permission_classes((IsAdminUser,))
def add_ingredient(request):
    
    if request.method == 'PUT':
        try:
            ingredient = IngredientsSerializer(data=request.data)
            if ingredient.is_valid():
                ingredient.save()
                return Response(status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes((IsAdminUser,))
def get_raw_material(request, id):

    if request.method == 'GET':
        try:
            raw_material = RawMaterials.objects.get(pk=id)
            serializer = RawMaterialsSerializer(raw_material)
            print(serializer.data)

            return Response(serializer.data)

        except Exception as e:
            print("Error : ",e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT',])
@permission_classes((IsAdminUser,))
def add_raw_material(request):
    
    if request.method == 'PUT':
        try:
            raw_material = RawMaterialsSerializer(data=request.data)
            if raw_material.is_valid():
                raw_material.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                print(raw_material.errors)
        except Exception as e:
            print("Error : ",e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes((IsAdminUser,))
def get_end_product(request, id):

    if request.method == 'GET':
        try:
            end_product = EndProducts.objects.get(pk=id)
            serializer = EndProductsSerializer(end_product)

            return Response(serializer.data)

        except Exception as e:
            print("Error : ",e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT',])
@permission_classes((IsAdminUser,))
def add_end_product(request):
    
    if request.method == 'PUT':
        try:
            end_product = EndProductsSerializer(data=request.data)
            if end_product.is_valid():
                end_product.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                print(end_product.errors)
        except Exception as e:
            print("Error : ",e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)
