from rest_framework import serializers

from .models import User


# send login data to front end
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
