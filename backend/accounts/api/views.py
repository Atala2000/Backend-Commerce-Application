from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from accounts.models import CustomUser
from accounts.api.serializers import UserSerializer


class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response(
                {"message": "User logged in successfully."}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Invalid email or password."}, status=status.HTTP_400_BAD_REQUEST
        )


class LogoutUserAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {"message": "User logged out successfully."}, status=status.HTTP_200_OK
        )



class UserAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User updated successfully."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(
            {"message": "User deleted successfully."}, status=status.HTTP_200_OK
        )
        