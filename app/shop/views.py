from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.models import Product

from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
	# total = serializers.IntegerField()

	class Meta:
		model = Shop
		fields = '__all__'
	
class ShopViewSet(viewsets.ModelViewSet):
	queryset = Shop.objects.all()
	serializer_class = ShopSerializer
	permission_classes = [IsAuthenticated]

	def create(self, request, *args, **kwargs):
		queryset = Shop.objects.filter(user=request.user.uuid)

		if queryset:
			return Response("Este usuario já possui produtos no carrinho")
		else:
			return super().create(request, *args, **kwargs)

	def list(self, request, *args, **kwargs):
		print(request.user.uuid)
		queryset = Shop.objects.filter(user=request.user.uuid)
		serializer = ShopSerializer(queryset, many=True)
		return Response(serializer.data)

    
      
	    
