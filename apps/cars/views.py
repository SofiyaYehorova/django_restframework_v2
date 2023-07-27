from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from apps.cars.models import CarModel

from .filters import car_filter_queryset
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    # pagination_class = PageNumberPagination
    # pagination_class = None

    def get_queryset(self):
        return car_filter_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
