from rest_framework import serializers
from .models import Order
from products.models import Product

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'title', 'price')

class OrderSerializer(serializers.ModelSerializer):
    product = ProductOrderSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
# 