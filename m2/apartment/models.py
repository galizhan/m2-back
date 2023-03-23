from django.db import models

from m2.building.models import Building
from m2.core.models import TimestampMixin


# Create your models here.

class Apartment(TimestampMixin):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='apartments', null=True)
    name = models.CharField(max_length=100)
    area = models.IntegerField()
    sold_area = models.IntegerField(default=0)
