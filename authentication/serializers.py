

from rest_framework import serializers
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active','is_superuser')


class UserValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    # def validate(self, data):
    #     if data['password'] != data['password_confirm']:
    #         raise serializers.ValidationError("Passwords don't match")
    #     return data