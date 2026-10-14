from django.urls import path

from .views import ComprarAPIView

urlpatterns = [
    path("comprar/", ComprarAPIView.as_view(), name="comprar"),
]
