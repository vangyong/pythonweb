from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    email = models.EmailField()


class Role(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
