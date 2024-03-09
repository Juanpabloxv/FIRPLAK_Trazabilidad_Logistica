from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

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

class PedidoViewSet(APIView):
    """API endpoint for viewing and interacting with Pedidos."""
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['numero_pedido', 'cliente']  # Allow searching by these fields
    ordering_fields = ['numero_pedido', 'fecha_ingreso']  # Allow ordering by these fields

    def get(self, request):
        """Get a list of Pedidos or retrieve a specific Pedido."""
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new Pedido."""
        serializer = PedidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
class LineaPedidoViewSet(APIView):
    """API endpoint for viewing and interacting with LineaPedidos."""

    def get(self, request, pk):
        """Get a specific LineaPedido."""
        try:
            linea_pedido = LineaPedido.objects.get(pk=pk)
            serializer = LineaPedidoSerializer(linea_pedido)
            return Response(serializer.data)
        except LineaPedido.DoesNotExist:
            return Response(status=404)

class DocumentoEntregaViewSet(APIView):
    """API endpoint for viewing and interacting with DocumentoEntregas."""

    def get(self, request, pk):
        """Get a specific DocumentoEntrega."""
        try:
            documento_entrega = DocumentoEntrega.objects.get(pk=pk)
            serializer = DocumentoEntregaSerializer(documento_entrega)
            return Response(serializer.data)
        except DocumentoEntrega.DoesNotExist:
            return Response(status=404)
        
class GuiaTransporteViewSet(APIView):
    """API endpoint for viewing and interacting with GuiaTransportes."""
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['numero_guia', 'cliente_destino']  # Allow searching by these fields
    ordering_fields = ['numero_guia', 'fecha_despacho']  # Allow ordering by these fields

    def get(self, request):
        """Get a list of GuiaTransportes."""
        guias_transporte = GuiaTransporte.objects.all()
        serializer = GuiaTransporteSerializer(guias_transporte, many=True)
        return Response(serializer.data)

class PruebaEntregaViewSet(APIView):
    """API endpoint for viewing and interacting with PruebaEntregas."""

    def get(self, request, pk):
        """Get a specific PruebaEntrega."""
        try:
            prueba_entrega = PruebaEntrega.objects.get(pk=pk)
            serializer = PruebaEntregaSerializer(prueba_entrega)
            return Response(serializer.data)
        except PruebaEntrega.DoesNotExist:
            return Response(status=404)

class FacturaViewSet(APIView):
    """API endpoint for viewing and interacting with Facturas."""
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['numero_factura']  # Allow searching by these fields
    ordering_fields = ['numero_factura', 'fecha_facturacion']  # Allow ordering by these fields

    def get(self, request):
        """Get a list of Facturas."""
        facturas = Factura.objects.all()
        serializer = FacturaSerializer(facturas, many=True)
        return Response(serializer.data)
    
class RadicacionFacturaViewSet(APIView):
    """API endpoint for viewing and interacting with RadicacionFacturas."""

    def get(self, request, pk):
        """Get a specific RadicacionFactura."""
        try:
            radicacion_factura = RadicacionFactura.objects.get(pk=pk)
            serializer = RadicacionFacturaSerializer(radicacion_factura)
            return Response(serializer.data)
        except RadicacionFactura.DoesNotExist:
            return Response(status=404)