from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'user',
            'employee_id',
            'name',
            'department',
            'salary',
            'proffesion',
            'employed_date',
        ]
