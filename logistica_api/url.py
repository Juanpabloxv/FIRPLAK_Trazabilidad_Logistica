from rest_framework.routers import DefaultRouter

from .views import (
    PedidoViewSet,
    LineaPedidoViewSet,
    DocumentoEntregaViewSet,
    GuiaTransporteViewSet,
    PruebaEntregaViewSet,
    FacturaViewSet,
    RadicacionFacturaViewSet,
)

router = DefaultRouter()

pedido_viewset = PedidoViewSet.as_view({'get': 'list', 'post': 'create'})
linea_pedido_viewset = LineaPedidoViewSet.as_view({'get': 'retrieve'})
documento_entrega_viewset = DocumentoEntregaViewSet.as_view({'get': 'retrieve'})
guia_transporte_viewset = GuiaTransporteViewSet.as_view({'get': 'list'})
prueba_entrega_viewset = PruebaEntregaViewSet.as_view({'get': 'retrieve'})
factura_viewset = FacturaViewSet.as_view({'get': 'list'})
radicacion_factura_viewset = RadicacionFacturaViewSet.as_view({'get': 'retrieve'})

router.register(r'pedidos', pedido_viewset, basename='pedido')
router.register(r'linea-pedidos', linea_pedido_viewset, basename='linea-pedido')
router.register(r'documento-entregas', documento_entrega_viewset, basename='documento-entrega')
router.register(r'guia-transportes', guia_transporte_viewset, basename='guia-transporte')
router.register(r'prueba-entregas', prueba_entrega_viewset, basename='prueba-entrega')
router.register(r'facturas', factura_viewset, basename='factura')
router.register(r'radicacion-facturas', radicacion_factura_viewset, basename='radicacion-factura')

urlpatterns = router.urls
