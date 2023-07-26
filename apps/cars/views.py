from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .filters import car_filter_queryset
from .serializers import CarSerializer
from apps.cars.models import CarModel


class CarListView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
