from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.BigIntegerField()
