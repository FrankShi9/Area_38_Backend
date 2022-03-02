from rest_framework import serializers

from .models import User

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {
            "username",
            "password",
            "get_absolute_url",
            "error_message",
            "get_image",
        }