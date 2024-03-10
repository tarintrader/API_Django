from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class Origen1(models.Model):
    origin = models.IntegerField()
    full_name = models.CharField(max_length=400)
    name = models.CharField(max_length=200)
    surnames = models.CharField(max_length=200)
    birthdate = models.DateTimeField()
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


