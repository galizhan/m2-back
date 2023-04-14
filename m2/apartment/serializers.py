from rest_framework import serializers

from m2.apartment.models import Apartment, ApartmentImage
from m2.building.serializers import BuildingSerializer


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    cover_image = serializers.SerializerMethodField(read_only=True)

    def get_cover_image(self, obj):
        image = obj.cover_image()
        if image:
            return ApartmentImageSerializer(image, context=self.context).data
        return None

    class Meta:
        model = Apartment
        fields = '__all__'

class ApartmentDetailedSerializer(ApartmentSerializer):
    building = BuildingSerializer(read_only=True)
