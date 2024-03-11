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
    """
    Vista para operaciones CRUD en el modelo Pedido.

    Attributes:
    - `queryset`: Conjunto de objetos Pedido disponibles para la vista.
    - `serializer_class`: Clase del serializador utilizada para convertir objetos Pedido a/desde representación JSON.
    """
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class LineaPedidoViewSet(viewsets.ModelViewSet):
    """
    Vista para operaciones CRUD en el modelo LineaPedido.

    Attributes:
    - `queryset`: Conjunto de objetos LineaPedido disponibles para la vista.
    - `serializer_class`: Clase del serializador utilizada para convertir objetos LineaPedido a/desde representación JSON.
    """
    queryset = LineaPedido.objects.all()
    serializer_class = LineaPedidoSerializer

class DocumentoEntregaViewSet(viewsets.ModelViewSet):
    """
    Vista para operaciones CRUD en el modelo DocumentoEntrega.

    Attributes:
    - `queryset`: Conjunto de objetos DocumentoEntrega disponibles para la vista.
    - `serializer_class`: Clase del serializador utilizada para convertir objetos DocumentoEntrega a/desde representación JSON.
    """
    queryset = DocumentoEntrega.objects.all()
    serializer_class = DocumentoEntregaSerializer

class GuiaTransporteViewSet(viewsets.ModelViewSet):
    """
    Vista para operaciones CRUD en el modelo GuiaTransporte.

    Attributes:
    - `queryset`: Conjunto de objetos GuiaTransporte disponibles para la vista.
    - `serializer_class`: Clase del serializador utilizada para convertir objetos GuiaTransporte a/desde representación JSON.
    """
    queryset = GuiaTransporte.objects.all()
    serializer_class = GuiaTransporteSerializer

class PruebaEntregaViewSet(viewsets.ModelViewSet):
    """
    Vista para operaciones CRUD en el modelo Factura.

    Attributes:
    - `queryset`: Conjunto de objetos Factura disponibles para la vista.
    - `serializer_class`: Clase del serializador utilizada para convertir objetos Factura a/desde representación JSON.
    """
    queryset = PruebaEntrega.objects.all()
    serializer_class = PruebaEntregaSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class RadicacionFacturaViewSet(viewsets.ModelViewSet):
    queryset = RadicacionFactura.objects.all()
    serializer_class = RadicacionFacturaSerializer