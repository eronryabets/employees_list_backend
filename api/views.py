
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
