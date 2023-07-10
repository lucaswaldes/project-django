"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django_crontab.views import CrontabView
from django.urls import path, include
from rest_framework import routers

from discord.views import discord_login, discord_login_redirect, logout, get_authenticated_user
from products.views import products, ProductViewSet
from shop.views import ShopViewSet
from checkout.views import CheckoutViewSet
from order.views import OrderViewSet, OrderViewSetAdmin

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'checkout', CheckoutViewSet, basename='checkout')


router.register(r'admin/order', OrderViewSetAdmin, basename='admin-order')
# router.register(r'pagamento/criar', create_payment, basename='create_payment')
# router.register(r'user', Teste, basename='get_authenticated_user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/', include(router.urls)),
    path('api/user/', get_authenticated_user, name="get_authenticated_user"),
    # path('auth/', home, name='auth'),
    path('auth/login/', discord_login, name='auth_login'),
    path('auth/login/redirect', discord_login_redirect, name="auth_login_redirect"),
    path('auth/logout', logout, name='logout'),
    path('products/', products, name="products"),
    # path('api/pagamento/criar/', create_payment, name="create_payment"),
    # path('api/notification/', notification, name='notification'),
    # path('api/payment/', get_payment, name='get_payment')
    # path('api/shop/', include('shop.urls')),
    # path('crontab/', CrontabView.as_view(), name='crontab'),
]