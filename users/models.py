from django.db import models
from Gym_Management.models import School

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)