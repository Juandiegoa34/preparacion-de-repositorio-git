from django.urls import path

from .views import ComprarAPIView, ProductosAPIView

urlpatterns = [
    path("productos/", ProductosAPIView.as_view(), name="productos"),
    path("comprar/", ComprarAPIView.as_view(), name="comprar"),
]
