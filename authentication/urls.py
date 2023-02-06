from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='Login'),
]