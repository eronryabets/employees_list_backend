from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeePagination(PageNumberPagination):
    page_size = 10


class EmployeeModelViewSet(ModelViewSet):
    # queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get_queryset(self):
        queryset = Employee.objects.all()

        # По умолчанию сортировка по id
        sort_by = self.request.query_params.get('sort_by', 'id')

        # Добавляем возможность сортировки по рейтингу или возрасту
        if sort_by == 'rating':
            queryset = queryset.order_by('-rating')  # Сортировка по убыванию рейтинга
        elif sort_by == 'age':
            queryset = queryset.order_by('-age')  # Сортировка по убыванию возраста
        else:
            queryset = queryset.order_by('id')  # По умолчанию по id

        search_query = self.request.query_params.get('search', None)
        if search_query:
            search_terms = search_query.split()
            if len(search_terms) == 1:
                queryset = queryset.filter(Q(first_name__icontains=search_terms[0]) |
                                           Q(last_name__icontains=search_terms[0]))
            else:
                queryset = queryset.filter(Q(first_name__icontains=search_terms[0]) &
                                           Q(last_name__icontains=search_terms[1]))

        return queryset
