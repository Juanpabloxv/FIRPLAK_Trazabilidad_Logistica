from rest_framework import routers
from django.urls import path, include

from .views import (
    PedidoViewSet,
    LineaPedidoViewSet,
    DocumentoEntregaViewSet,
    GuiaTransporteViewSet,
    PruebaEntregaViewSet,
    FacturaViewSet,
    RadicacionFacturaViewSet,
)

router = routers.DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'lineas-pedido', LineaPedidoViewSet)
router.register(r'documentos-entrega', DocumentoEntregaViewSet)
router.register(r'guias-transporte', GuiaTransporteViewSet)
router.register(r'pruebas-entrega', PruebaEntregaViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'radicaciones-factura', RadicacionFacturaViewSet)

urlpatterns = router.urls