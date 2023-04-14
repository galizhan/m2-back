from rest_framework.viewsets import ModelViewSet

from m2.investment.models import Investment, Favourite
from m2.investment.serializers import UserInvestmentSerializer, UserFavouriteSerializer


class InvestmentViewSet(ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = UserInvestmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user__id=self.request.user.id)

class FavouriteViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = UserFavouriteSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user__id=self.request.user.id)
