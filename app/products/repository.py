from .models import Product
import datetime
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

class RepositoryProduct:
    def create_product(self, request):
        if request.user.is_admin == False:
            return request
        else: 
            return {"error": "You do not have permission to access this route."}
        
    def destroy_product(self, request, pk):
        try:
            product = Product.objects.get(uuid=pk)
        except: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.user.is_admin == False:
            return Response("Error: Only admins can access this route",status=status.HTTP_403_FORBIDDEN)
        
        product.deleted = True
        product.deleted_at = datetime.datetime.now()
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
