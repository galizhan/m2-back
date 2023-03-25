from rest_framework import serializers

from m2.apartment.models import Apartment, ApartmentImage


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
