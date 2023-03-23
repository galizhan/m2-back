from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=300)

class Level(models.Model):
    name = models.CharField(max_length=300)
    investment_price = models.IntegerField()
    icon_active = models.FileField()
    icon_inactive = models.FileField()
