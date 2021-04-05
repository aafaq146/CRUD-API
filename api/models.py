from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    Empname = models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    salary = models.IntegerField()

