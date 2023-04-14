from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from m2.apartment.models import Apartment
from m2.building.models import Building
from m2.core.models import TimestampMixin
from m2.main.models import Level
from m2.users.models import User


class Investment(TimestampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')
    total_price = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='investments')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_investment')

class InvestmentDocuments(TimestampMixin):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='documents')


class Favourite(TimestampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='favourites')
@receiver(post_save, sender=Investment)
def update_users_data(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.investment_price += instance.total_price
        level = Level.objects.filter(investment_price__gte=user.investment_price, number__lt=user.level.number)
        if level.exists():
            user.level = level[0]
        user.save()

        apartment = instance.apartment
        apartment.sold_area += instance.area
        apartment.save()

        building = apartment.building
        building.total_sold_area += instance.area
        building.save()
