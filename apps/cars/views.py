from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .filters import car_filter_queryset
from .serializers import CarSerializer
from apps.cars.models import CarModel


# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         # cars = CarModel.objects.all()
#         # serializer = CarSerializer(cars, many=True)
#         # return Response(serializer.data, status.HTTP_200_OK)
#         # qs = CarModel.objects.all()
#         # qs = CarModel.objects.all().filter(price__in=[26100, 27800, 86000])
#         # qs = CarModel.objects.all().filter(price__in=[26100, 27800, 86000]).filter(brand__istartswith='k')
#         # qs = CarModel.objects.all().filter(price__in=[26100, 27800, 86000], brand__icontains='a')
#         # qs = CarModel.objects.filter(Q(price=86000) & Q(brand='Ford'))
#         # qs = CarModel.objects.filter(Q(price=86000) | Q(brand='Ford'))
#         # qs = CarModel.objects.filter(Q(price=86000) | Q(brand='Ford')).order_by('year', 'price')
#         # qs = CarModel.objects.filter(Q(price=86000) | Q(brand='Ford')).order_by('year', 'price').reverse()
#         # qs = CarModel.objects.filter(Q(price=86000) | Q(brand='Ford')).order_by('year', 'price').reverse().exclude(price=0)
#         # qs = CarModel.objects.filter(Q(price=86000) | Q(brand='Ford')).order_by('year', 'price').reverse().exclude(price=0)[1:4]
#         # serializer = CarSerializer(qs, many=True)
#         # return Response(serializer.data, status.HTTP_200_OK)
#         # # qs = qs.filter(brand__istartswith='m')
#         # print(qs.query)
#         # print(qs)
#         # return Response('ok', status.HTTP_200_OK)
#         qs = car_filter_queryset(self.request.query_params)
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)

# class CarListCreateView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         qs = car_filter_queryset(self.request.query_params)
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)

# def post(self, *args, **kwargs):
#     data = self.request.data
#     serializer = CarSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status.HTTP_201_CREATED)

# class CarListView(GenericAPIView, ListModelMixin):
#
#     def get_queryset(self):
#         return car_filter_queryset(self.request.query_params)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

class CarListView(ListAPIView):

    def get_queryset(self):
        return car_filter_queryset(self.request.query_params)


# class CarRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         car = get_object_or_404(CarModel, pk=pk)
#
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data: dict = self.request.data
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         car = get_object_or_404(CarModel, pk=pk)
#
#         serializer = CarSerializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data: dict = self.request.data
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         car = get_object_or_404(CarModel, pk=pk)
#
#         serializer = CarSerializer(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         #     car.delete()
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#
#         car = get_object_or_404(CarModel, pk=pk)
#         car.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     # lookup_field = 'my_id' # if you don't use 'pk'
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         data: dict = self.request.data
#         car = self.get_object()
#         serializer = CarSerializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         car = self.get_object()
#         data = self.request.data
#         serializer = CarSerializer(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         car = self.get_object()
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
