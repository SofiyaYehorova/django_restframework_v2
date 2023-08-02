from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from core.permissions.is_super_user import IsSuperUser

from apps.cars.models import CarModel

from .filters import CarFilter
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    # queryset = CarModel.my_objects.get_only_jeep()
    # queryset = CarModel.my_objects.get_cars_by_auto_park_id(1).year_less(2009)
    filterset_class = CarFilter
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsSuperUser,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
