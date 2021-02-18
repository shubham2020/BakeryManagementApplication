from rest_framework import serializers

from bakery.models import (
    Units,
    Ingredients,
    BakeryItems,
    Composition,
    RawMaterials,
    EndProducts
)


'''
Serializers for getting and putting the Bakery Items details
'''
class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = ['name']

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id','name', 'price']

class CompositionSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(queryset=Ingredients.objects.all())
    units = serializers.PrimaryKeyRelatedField(queryset=Units.objects.all())
    
    class Meta:
        model = Composition
        fields = ['ingredients','quantity', 'units']

class BakeryItemsSerializer(serializers.ModelSerializer):
    composition_set = CompositionSerializer(many=True)
    cost_price = serializers.SerializerMethodField(method_name='get_cost_price', read_only=True)
    selling_price = serializers.SerializerMethodField(method_name='get_selling_price', read_only=True)

    class Meta:
        model = BakeryItems
        fields = ['name', 'composition_set', 'profit', 'discount', 'cost_price', 'selling_price']
        depth = 1

    def get_cost_price(self, item):
        sum = 0
        for ing in item.composition_set.all():
            sum += ing.quantity*ing.ingredients.price
        
        return sum

    def get_selling_price(self, item):
        cp = self.get_cost_price(item)
        profit = item.profit
        discount = item.discount

        return ((cp*(1+(profit/100)))*(1-discount/100))

    def create(self, validated_data):
        composition_set = validated_data.pop('composition_set')
        bakeryItem = BakeryItems(**validated_data)
        bakeryItem.save()
        for composite in composition_set:
            Composition.objects.create(bakeryItem=bakeryItem, 
                                       ingredients=composite.get('ingredients'),
                                       quantity=composite.get('quantity'),
                                       units=composite.get('units'))

        return bakeryItem

'''
Serializers for inventory management
'''

class RawMaterialsSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(queryset=Ingredients.objects.all())
    units = serializers.PrimaryKeyRelatedField(queryset=Units.objects.all())

    class Meta:
        model = RawMaterials
        fields = ['ingredients', 'quantity', 'units']


class EndProductsSerializer(serializers.ModelSerializer):
    bakeryItems = serializers.PrimaryKeyRelatedField(queryset=BakeryItems.objects.all())
    units = serializers.PrimaryKeyRelatedField(queryset=Units.objects.all(), required=False)

    class Meta:
        model = EndProducts
        fields = ['bakeryItems', 'quantity', 'units']


'''
Serializer for user list generation
'''
class UserProductListSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('get_selling_price')

    class Meta:
        model = BakeryItems
        fields =['name', 'price']

    def get_cost_price(self, item):
        sum = 0
        for ing in item.composition_set.all():
            sum += ing.quantity*ing.ingredients.price
        
        return sum

    def get_selling_price(self, item):
        cp = self.get_cost_price(item)
        profit = item.profit
        discount = item.discount

        return ((cp*(1+(profit/100)))*(1-discount/100))