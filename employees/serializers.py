from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'age',
            'position',
            'profession',
            'years_worked',
            'phone_number',
            'email',
            'facebook_link',
        )
