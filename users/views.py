import time
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from authentication.serializers import UserResponseSerializer

from helpers.response_helpers import api_success_response

# Create your views here.
class UserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        time.sleep(1)
        return api_success_response(UserResponseSerializer(request.user).data,"User Profile",HTTP_200_OK)