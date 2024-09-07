from django.urls import path

from api.views import EmployeeListApiView

app_name = 'api'

urlpatterns = [
    path('employee-list/', EmployeeListApiView.as_view(), name='employee_list'),
]