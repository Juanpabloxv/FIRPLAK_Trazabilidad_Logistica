from rest_framework import viewsets

from .models import (Pedido, LineaPedido, DocumentoEntrega, GuiaTransporte, 
                     PruebaEntrega, Factura, RadicacionFactura)
from .serializers import (
    PedidoSerializer,
    LineaPedidoSerializer,
    DocumentoEntregaSerializer,
    GuiaTransporteSerializer,
    PruebaEntregaSerializer,
    FacturaSerializer,
    RadicacionFacturaSerializer,
)

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class LineaPedidoViewSet(viewsets.ModelViewSet):
    queryset = LineaPedido.objects.all()
    serializer_class = LineaPedidoSerializer

class DocumentoEntregaViewSet(viewsets.ModelViewSet):
    queryset = DocumentoEntrega.objects.all()
    serializer_class = DocumentoEntregaSerializer

class GuiaTransporteViewSet(viewsets.ModelViewSet):
    queryset = GuiaTransporte.objects.all()
    serializer_class = GuiaTransporteSerializer

class PruebaEntregaViewSet(viewsets.ModelViewSet):
    queryset = PruebaEntrega.objects.all()
    serializer_class = PruebaEntregaSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class RadicacionFacturaViewSet(viewsets.ModelViewSet):
    queryset = RadicacionFactura.objects.all()
    serializer_class = RadicacionFacturaSerializer