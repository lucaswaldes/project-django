from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from .serializers import ProductSerializer
from .models import Product
from .repository import RepositoryProduct


def products(request: HttpRequest):
	print(request.user)
	return JsonResponse({"message": "Olá Mundo"})


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().filter(deleted=False)
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]


	def list(self, request, *args, **kwargs):
		print(request.user)
		return super().list(request, *args, **kwargs)

	def create(self, request, *args, **kwargs):
		request = RepositoryProduct.create_product(self, request)

		if type(request) == dict:
			if 'error' in request:
				return Response(status=status.HTTP_400_BAD_REQUEST, data=request['error'])
		return super().create(request, *args, **kwargs)
	
	def destroy(self, request, pk, *args, **kwargs):
		request = RepositoryProduct.destroy_product(self, request, pk)
		
		return request
	
	def update(self, request, *args, **kwargs):
		print('Foda')
		return super().update(request, *args, **kwargs)
