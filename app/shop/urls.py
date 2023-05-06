from django.urls import path
from .views import ShopViewSet

urlpatterns = [
    path('<int:id>', ShopViewSet.as_view(), name='shop')
]