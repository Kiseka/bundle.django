from django.shortcuts import render
from rest_framework.views import APIView
from authentication.serializers import UserValidationSerializer
from django.contrib.auth import login, authenticate
from helpers.response_helpers import api_success_response,api_error_response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Override the post method to handle login with a custom user model
        serializer = UserValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)
        if user is None:
            return api_error_response("Login failed","Unauthorized",401)

        login(request, user)

        refresh = RefreshToken.for_user(user)
        return api_success_response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })