from django.forms.models import model_to_dict
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import EmployeeSerializer
from .models import Employee
import json


@api_view(["GET"])
def all_employees(request):
    employees = Employee.objects.all()
    # data = [model_to_dict(employee) for employee in employees]
    if employees:
        data = EmployeeSerializer(employees, many=True).data
    # return JsonResponse(data, safe=False)
    return Response(data)

@api_view(["POST"])
def post_employee(request):
    employee = request.data
    serialize = EmployeeSerializer(data=employee)

    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)
