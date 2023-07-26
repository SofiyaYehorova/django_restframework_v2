from django.urls import path


from .views import CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
    # path('cars/<int:my_id>', CarRetrieveUpdateDestroyView.as_view()).
]
