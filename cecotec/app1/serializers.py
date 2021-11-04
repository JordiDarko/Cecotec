from rest_framework import serializers
from app1.models import Product, Item, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'description']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'product', 'quantity', 'ordered']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'shipping_charges', 'observations', 'ordered']
