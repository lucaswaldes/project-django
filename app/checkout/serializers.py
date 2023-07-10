from rest_framework import serializers

class CheckoutSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    value = serializers.IntegerField(required=True)
