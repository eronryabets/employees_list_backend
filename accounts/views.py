from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse
import datetime


# Регистрация
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user_group = Group.objects.get(name='user')  # Назначаем группу по умолчанию
        user.groups.add(user_group)


# Получение UPDATE данных текущего пользователя
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Отправляем данные о пользователе, включая его роль
        return Response({
            'username': user.username,
            'email': user.email,
            'role': 'admin' if user.is_staff else 'user',
        })


class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logout successful"},
                            status=status.HTTP_205_RESET_CONTENT)

        # Удаление токенов из cookies
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data

        # Получаем access и refresh токены
        access_token = data.get('access')
        refresh_token = data.get('refresh')

        # Создаем ответ с пустым телом (мы отправляем токены через cookies)
        response = JsonResponse({"message": "Login successful"})

        # Устанавливаем токены в httpOnly cookies
        access_expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        refresh_expiry = datetime.datetime.utcnow() + datetime.timedelta(days=1)

        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=True,  # Установи True для HTTPS
            samesite='Lax',
            expires=access_expiry
        )

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            secure=True,  # Установи True для HTTPS
            samesite='Lax',
            expires=refresh_expiry
        )

        return response
