from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer


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


# Выход из системы
class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Successfully logged out"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)



# class LogoutView(APIView):
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()  # Добавляем refresh_token в чёрный список
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except KeyError:
#             return Response({"error": "'refresh_token' not provided"}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
