from django.db import models

# Create your models here.
class MenuItems(models.Model):
    itemName = models.CharField(max_length=200)
    categorey = models.CharField(max_length=300)
    year = models.IntegerField()

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()