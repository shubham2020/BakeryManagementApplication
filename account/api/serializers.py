from rest_framework import serializers
from django.contrib.auth.models import User

from bakery.models import BakeryItems
from account.models import OrderedItems, Orders

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': { 'write_only': True }
        }

    def save(self, **kwargs):
        user = User.objects.create_user(username=self.validated_data.get('username'),
                                        first_name=self.validated_data.get('first_name'),
                                        last_name=self.validated_data.get('last_name'),
                                        email=self.validated_data.get('email'),
                                        password=self.validated_data.get('password'))

        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


class OrderedItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedItems
        fields = ['item', 'quantity']

class OrdersSerializer(serializers.ModelSerializer):
    ordereditems = OrderedItemsSerializer(many=True)
    
    class Meta:
        model = Orders
        fields = ['user', 'ordereditems']
    
    def create(self, validated_data):
        ordereditems = validated_data.pop('ordereditems')
        order = Orders.objects.create(**validated_data)
        for item in ordereditems:
            OrderedItems.objects.create(order=order, item=item['item'], quantity=item['quantity'])
        return order


class OrderHistorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Orders
        fields = ['user', 'date', 'ordereditems_set']


class PreBillSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('get_selling_price')
    item = serializers.ReadOnlyField(source='item.name')

    class Meta:
        model = OrderedItems
        fields =['item', 'quantity', 'price']

    def get_cost_price(self, item):
        sum = 0
        for ing in item.composition_set.all():
            sum += ing.quantity*ing.ingredients.price
        
        return sum

    def get_selling_price(self, item):
        item = item.item
        cp = self.get_cost_price(item)
        profit = item.profit
        discount = item.discount

        return ((cp*(1+(profit/100)))*(1-discount/100))

class BillSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Orders
        fields = ['name', 'date']
        depth = 1

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['orders_set', 'username', 'first_name', 'email']
        depth = 2