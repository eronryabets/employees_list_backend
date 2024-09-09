
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
