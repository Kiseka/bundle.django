from django.db.migrations import serializer
from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .models import Todo
from helpers.response_helpers import api_error_response, api_success_response
from .serializers import TodoSerializer, TodoStatusSerializer

# Create your views here.
class TodoListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return api_success_response(serializer.data)
    
class TodoCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid()
        if serializer.errors:
            return api_error_response(serializer.errors,"Validation Error", HTTP_400_BAD_REQUEST)
        else:
            serializer.validated_data['user'] = request.user
            serializer.save()
            return api_success_response(serializer.data,"TODO CREATED SUCCESSFULLY",HTTP_201_CREATED)
        
class TodoUpdateStatusView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, id):
        status_serializer = TodoStatusSerializer(data = request.data)
        status_serializer.is_valid()
        if status_serializer.errors:
            return api_error_response(status_serializer.errors,"Validation Error", HTTP_400_BAD_REQUEST)
        
        queryset = Todo.objects.filter(id=id)
        if queryset:
            todo = queryset[0]
            status_serializer.update(todo, status_serializer.validated_data)
            todo_serializer = TodoSerializer(queryset[0])
            return api_success_response(todo_serializer.data, "Todo Status Updated", HTTP_200_OK)
        else:
            return api_error_response([{"error": "Todo not found"},],"Todo does not exist", HTTP_400_BAD_REQUEST)

    
class TodoDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, id):
        queryset = Todo.objects.filter(id=id)
        print(queryset)
        if queryset:
            serializer = TodoSerializer(queryset[0])
            return api_success_response(serializer.data, "TODO DELETED SUCCESSFULLY", HTTP_200_OK)
        else:
            return api_error_response([{"error": "Todo not found"},],"Todo does not exist", HTTP_400_BAD_REQUEST)

        
class TodoDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            serializer = TodoSerializer(todo)
            return api_success_response(serializer.data, "TODO DELETED SUCCESSFULLY", HTTP_200_OK)
        except Todo.DoesNotExist:
            return api_error_response([{"error": "Todo not found"},],"Todo does not exist", HTTP_400_BAD_REQUEST)
