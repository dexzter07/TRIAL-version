from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE, related_name='items')
    age = models.CharField(max_length=34)

    def __str__(self):
        return self.name.username

