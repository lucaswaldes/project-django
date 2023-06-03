from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import logout

class AuthenticationExpirationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if user.is_authenticated:
            last_login = user.last_login
            current_time = timezone.now()
            expiration_time = last_login + timedelta(hours=1)

            if current_time > expiration_time:
                logout(request)
 
        response = self.get_response(request)
        return response
