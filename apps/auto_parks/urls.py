from django.urls import path

from .views import AutoParkListCreateView, AutoParkCarListCreateView, AutoParkRetrieveUpdateDestroy

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroy.as_view()),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view()),
]
