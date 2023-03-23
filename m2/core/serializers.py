from django.utils import timezone
from rest_framework import serializers


class DateTimeFieldWihTZ(serializers.DateTimeField):
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super().to_representation(value)
