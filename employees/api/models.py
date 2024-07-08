from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    # user = models.OneToOneField(to)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=180)
    department = models.CharField(max_length=200)
    salary = models.FloatField()
    proffesion = models.CharField(max_length=200)
    employed_date = models.DateField()

    def __str__(self):
        return str(self.employee_id)
