from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from discord.models import DiscordUser
from rest_framework import serializers
from django.utils import timezone
from rest_framework_simplejwt.settings import (
                api_settings as jwt_settings,
            )

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user:DiscordUser):
        token = super().get_token(user)
        user_dict = {"email":user.email,
                     'id':str(user.uuid),
                     "first_name": user.first_name,
		             "last_name": user.last_name,
                     }
        if user.is_admin:
            user_dict['role'] = ['admin','public']
        else:
            user_dict['role'] = ['public']
        
        if hasattr(user,'avatar'):
            user_dict['picture'] = user.avatar

        token['user'] = user_dict
        return token


class CustomJWTSerializer(serializers.Serializer):

    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField()
    expires_at = serializers.TimeField(read_only=True)

    def get_initial(self):
        self.expires_at = str(round((timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME - timezone.now()).total_seconds() * 1000))
        return super().get_initial()