from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login as Login_process
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.response import Response
from rest_framework import status

from .models import DiscordUser
from .serializers import UserSerializer

from rest_framework import viewsets

from collections.abc import Iterable

import requests

auth_url = "https://discord.com/api/oauth2/authorize?client_id=906896716895223838&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fauth%2Flogin%2Fredirect&response_type=code&scope=identify%20email"

def home(request: HttpRequest) -> HttpResponse:
    print(request.user)

    return JsonResponse({"message": "Hello World"})

# @method_decorator(login_required, name='dispatch')
# class Teste(viewsets.ModelViewSet):
#     queryset = DiscordUser.objects.all()
#     serializer_class = UserSerializer

#     def list(self, request, *args, **kwargs):
#         print(request.user)
#         return super().list(request, *args, **kwargs)
@login_required(login_url='/auth/login')
def get_authenticated_user(request: HttpRequest):
    print(request.user)
    user = request.user
    return JsonResponse({
        "id": user.discord_id,
        "tag": user.discord_tag,
        "email": user.email,
        "avatar": user.avatar,
        "locale": user.locale,
        # "banner": user.banner,
        # "banner_color": user.banner_color,
        })

def login(request: HttpRequest):
    return redirect(auth_url)

def login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    
    user = exchange_code(code)

    discord_user = authenticate(request, user=user)
    if isinstance(discord_user, Iterable):
        discord_user = list(discord_user).pop()


    # print(discord_user)
    Login_process(request, discord_user, backend='discord.auth.AuthenticationBackend')
    print(request.user.is_authenticated)
    return redirect("/api/user")

def exchange_code(code: str):
    data = {
        "client_id": "906896716895223838",
        "client_secret": "5dT_BPpG8kb49VgeNAGI9p8iQ7Rbd-Fh",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/auth/login/redirect",
        "scope": "identify"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    # print(response)
    creadentials = response.json()
    access_token = creadentials['access_token']
    response = requests.get('https://discord.com/api/v6/users/@me', headers={
        'Authorization': 'Bearer %s' % access_token
    })
    # print(response)
    user = response.json()
    # print(user)
    return user