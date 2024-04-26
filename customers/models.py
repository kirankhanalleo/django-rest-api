from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=20)
    address=models.TextField()
    age=models.IntegerField()
    phone_numer = models.CharField(max_length=10)
