from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, LogoutView, UserProfileView, CustomTokenObtainPairView, CookieTokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
