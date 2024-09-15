from django.urls import path, include

from rest_framework import routers

from api.views import EmployeeModelViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'employee', EmployeeModelViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
