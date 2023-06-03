from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().filter(deleted=False)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def list(self, request, *args, **kwargs):
        queryset = Order.objects.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)