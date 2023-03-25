from rest_framework import serializers

from m2.main.models import City,Level


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class LevelSerializerDetailed(serializers.ModelSerializer):
