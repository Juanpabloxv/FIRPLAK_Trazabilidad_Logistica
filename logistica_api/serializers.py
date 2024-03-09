from rest_framework import serializers
from .models import Pedido, LineaPedido, DocumentoEntrega, GuiaTransporte, PruebaEntrega, Factura, RadicacionFactura

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class LineaPedidoSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(read_only=True)
    class Meta:
        model = LineaPedido
        fields = '__all__'

class DocumentoEntregaSerializer(serializers.ModelSerializer):
    linea_pedido = LineaPedidoSerializer(read_only=True)
    class Meta:
        model = DocumentoEntrega
        fields = '__all__'

class GuiaTransporteSerializer(serializers.ModelSerializer):
    documentos_entrega = DocumentoEntregaSerializer(many=True, read_only=True)
    class Meta:
        model = GuiaTransporte
        fields = '__all__'

class PruebaEntregaSerializer(serializers.ModelSerializer):
    guia_transporte = GuiaTransporteSerializer(read_only=True)
    class Meta:
        model = PruebaEntrega
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    documentos_entrega = DocumentoEntregaSerializer(many=True, read_only=True)
    class Meta:
        model = Factura
        fields = '__all__'

class RadicacionFacturaSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer(read_only=True)
    class Meta:
        model = RadicacionFactura
        fields = '__all__'