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
from django.urls import path, include
from rest_framework import routers

from discord.views import home, login, login_redirect, get_authenticated_user
from products.views import products, ProductViewSet
from shop.views import ShopViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'shop', ShopViewSet, basename='shop')
# router.register(r'user', Teste, basename='get_authenticated_user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/', include(router.urls)),
    path('api/user/', get_authenticated_user, name="get_authenticated_user"),
    path('auth/', home, name='auth'),
    path('auth/login/', login, name='auth_login'),
    path('auth/login/redirect', login_redirect, name="auth_login_redirect"),
    path('products/', products, name="products"),
    # path('api/shop/', include('shop.urls')),
]
