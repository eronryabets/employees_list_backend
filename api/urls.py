from django.urls import path, include

from rest_framework import routers

from api.views import EmployeeModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'employee', EmployeeModelViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]