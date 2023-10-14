from django.db import models

class RegStu(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
