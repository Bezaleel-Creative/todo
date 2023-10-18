from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Todo_list(models.Model):
    tasks = models.CharField(max_length=1000, null=True)
    start_time = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False, null=True)

    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
