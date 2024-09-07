from rest_framework.generics import ListAPIView

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeListApiView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
