from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as Login_process, logout as logout_user

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

import requests
from collections.abc import Iterable
@csrf_exempt
def discord_login(request):
    return redirect('https://discord.com/api/oauth2/authorize?client_id=906896716895223838&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fauth%2Flogin%2Fredirect&response_type=code&scope=identify%20email')

@csrf_exempt
def discord_login_redirect(request):
    code = request.GET.get('code')

    data = {
        'client_id': '906896716895223838',
        'client_secret': '5dT_BPpG8kb49VgeNAGI9p8iQ7Rbd-Fh',
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/auth/login/redirect',
        'scope': 'identify email'
    }

    response = requests.post('https://discord.com/api/oauth2/token', data=data)
    response_json = response.json()

    access_token = response_json['access_token']

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    user_response = requests.get('https://discord.com/api/users/@me', headers=headers)
    user_data = user_response.json()


    user = authenticate(request, user=user_data)
    if isinstance(user, Iterable):
        user = list(user).pop()

    Login_process(request, user, backend='discord.auth.AuthenticationBackend')
    return redirect('http://localhost:5173/')

def logout(request):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = 'http://localhost:5173'  # Substitua pela origem correta do seu aplicativo React
    response['Access-Control-Allow-Credentials'] = 'true'
    logout_user(request)
    return HttpResponse(200)

@login_required
def get_authenticated_user(request):
    user = request.user
    # print(user.__dict__)
    return JsonResponse({
        'id': user.discord_id,
        'tag': user.discord_tag,
        'email': user.email,
        'username': user.username,
        'avatar': user.avatar
    })