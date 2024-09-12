from rest_framework.viewsets import ModelViewSet
from django.db.models import Q  # Для сложных запросов
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()  # Это базовый queryset, его можно оставить
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all().order_by('id')
        search_query = self.request.query_params.get('search', None)
        if search_query:
            search_terms = search_query.split()
            if len(search_terms) == 1:
                # Если одно слово, ищем либо по имени, либо по фамилии
                queryset = queryset.filter(Q(first_name__icontains=search_terms[0]) |
                                           Q(last_name__icontains=search_terms[0]))
            else:
                # Если два слова, ищем по имени и фамилии
                queryset = queryset.filter(Q(first_name__icontains=search_terms[0]) &
                                           Q(last_name__icontains=search_terms[1]))
        return queryset
