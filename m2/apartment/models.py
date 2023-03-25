from django.db import models

from m2.building.models import Building
from m2.core.models import TimestampMixin


# Create your models here.

class Apartment(TimestampMixin):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='apartments', null=True)
    name = models.CharField(max_length=100)
    area = models.IntegerField()
    sold_area = models.IntegerField(default=0)

    def cover_image(self):
        images = self.images.filter(is_cover=True)
        if images.exists():
            return images[0]
        return None

    def __str__(self):
        return self.name
class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='apartment_images')
    is_cover = models.BooleanField(default=False)
