from rest_framework import serializers

from m2.main.models import City, Level


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    is_locked = serializers.SerializerMethodField()

    def get_is_locked(self, obj):
        return self.context['request'].user.level.number > obj.number

    class Meta:
        model = Level
        fields = '__all__'


class LevelSerializerDetailed(LevelSerializer):
    buildings = serializers.SerializerMethodField()

    def get_buildings(self, obj):
        from m2.building.serializers import BuildingSerializer
        return BuildingSerializer(obj.buildings.all(), many=True, context=self.context).data
    class Meta:
        model = Level
        fields = ['id', 'name', 'buildings', 'is_locked', 'icon_active', 'icon_inactive']
        depth = 1
