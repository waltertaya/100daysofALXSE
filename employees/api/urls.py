from django.urls import path
from .views import all_employees, post_employee


urlpatterns = [
    path('', all_employees),
    path('post/', post_employee)
]