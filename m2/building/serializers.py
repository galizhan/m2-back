from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import BuildingPrice, Building, BuildingImage, BuildingAdditional


class BuildingPriceSerializer(ModelSerializer):
    cover_image = serializers.SerializerMethodField()

    def get_cover_image(self, obj):
        return obj.cover_image
    class Meta:
        model = BuildingPrice
        fields = '__all__'


class BuildingSerializer(ModelSerializer):
    price = BuildingPriceSerializer(many=True)

    class Meta:
        model = Building
        fields = '__all__'


class BuildingImageSerializer(ModelSerializer):
    class Meta:
        model = BuildingImage
        fields = '__all__'


class BuildingAdditionalSerializer(ModelSerializer):
    class Meta:
        model = BuildingAdditional
        fields = '__all__'


class BuildingDetailSerializer(BuildingSerializer):
    images = BuildingImageSerializer(many=True)
    additionals = BuildingAdditionalSerializer(many=True)
