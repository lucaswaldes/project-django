from rest_framework import serializers
from .models import DiscordUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = '__all__'
# 