from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from m2.building.choices import BuildingAdditionalChoices
from m2.core.models import TimestampMixin


# Create your models here.
class Building(TimestampMixin):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    pass_date = models.DateField()
    income_percentage = models.IntegerField()
    city = models.ForeignKey('main.City', on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey('main.Level', on_delete=models.SET_NULL, null=True)
    total_area = models.IntegerField()
    total_sold_area = models.IntegerField(default=0)
    description = RichTextUploadingField()
    average_price = models.IntegerField()

    def cover_image(self):
        cover_image = self.images.filter(is_cover=True)
        if cover_image.exists():
            return cover_image.first().url
        return None


class BuildingImage(models.Model):
    building = models.ForeignKey(Building, related_name='images', on_delete=models.CASCADE)
    image = models.FileField()
    is_cover = models.BooleanField(default=False)

    class Meta:
        ordering = ['is_cover']


class BuildingAdditional(models.Model):
    building = models.ForeignKey(Building, related_name='additionals', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=BuildingAdditionalChoices.choices)
    title = models.CharField(max_length=255)
    external_url = models.URLField()
    description = RichTextUploadingField()


class BuildingPrice(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField()
