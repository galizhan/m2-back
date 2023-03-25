from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import BuildingPrice, Building, BuildingImage, BuildingAdditional
from ..main.serializers import CitySerializer, LevelSerializer


class BuildingPriceSerializer(ModelSerializer):
    class Meta:
        model = BuildingPrice
        fields = '__all__'
class BuildingImageSerializer(ModelSerializer):
    class Meta:
        model = BuildingImage
        fields = '__all__'

class BuildingSerializer(ModelSerializer):
    price_changes = BuildingPriceSerializer(many=True)
    city = CitySerializer()
    level = LevelSerializer()
    cover_image = serializers.SerializerMethodField('get_cover_image')

    def get_cover_image(self, obj):
        image = obj.cover_image()
        if image:
            return BuildingImageSerializer(image, context=self.context).data
        return None
    class Meta:
        model = Building
        fields = '__all__'





class BuildingAdditionalSerializer(ModelSerializer):
    class Meta:
        model = BuildingAdditional
        fields = '__all__'


class BuildingDetailSerializer(BuildingSerializer):
    images = BuildingImageSerializer(many=True)
    additionals = BuildingAdditionalSerializer(many=True)
