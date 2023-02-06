from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListAPIView.as_view(), name='Todo List'),
    path('create/', views.TodoCreateAPIView.as_view(), name="Todo Create"),
    path('delete/<int:id>/', views.TodoDeleteAPIView.as_view(), name="Todo Delete"),
    path('details/<int:id>/', views.TodoDetailAPIView.as_view(), name="Todo Details"),
    path('update/<int:id>/', views.TodoUpdateStatusView.as_view(), name="Todo Update"),
]