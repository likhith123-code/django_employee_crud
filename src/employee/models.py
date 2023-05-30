from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.TextField()
    city = models.TextField()

class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    description = models.TextField()
