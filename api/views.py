from rest_framework.response import Response
from rest_framework.views import APIView


class ComprarAPIView(APIView):
    def get(self, request):
        return Response({
            "mensaje": "Endpoint de compras disponible",
            "estado": "ok",
            "servicio": "Tienda API",
        })

    def post(self, request):
        return Response({
            "mensaje": "Compra recibida",
            "estado": "ok",
            "datos": request.data,
        }, status=201)
