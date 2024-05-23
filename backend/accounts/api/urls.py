from django.urls import path
from .views import RegisterUserAPIView, LoginUserAPIView, LogoutUserAPIView, UserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
    path('user/', UserAPIView.as_view(), name='user'),
]
