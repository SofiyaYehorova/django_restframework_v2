from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from core.permissions.is_super_user import IsSuperUser

from apps.cars.models import CarModel

from .filters import CarFilter
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (IsSuperUser,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
