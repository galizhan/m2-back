from rest_framework.serializers import ModelSerializer

from m2.apartment.serializers import ApartmentSerializer, ApartmentDetailedSerializer
from m2.building.serializers import BuildingSerializer
from m2.investment.models import Investment, Favourite, InvestmentDocuments

class InvestmentDocumentSerializer(ModelSerializer):
    class Meta:
        model = InvestmentDocuments
        fields = '__all__'
class UserInvestmentSerializer(ModelSerializer):
    apartment = ApartmentDetailedSerializer()
    documents = InvestmentDocumentSerializer(many=True)
    class Meta:
        model = Investment
        fields = '__all__'

class UserFavouriteSerializer(ModelSerializer):
    building = BuildingSerializer()
    class Meta:
        model = Favourite
        fields = '__all__'
