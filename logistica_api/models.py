from django.db import models
from django.forms import ValidationError
from django.db.models import Min


class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField()
    cliente = models.CharField(max_length=100, blank=False)
    estado_pedido = models.CharField(max_length=20, choices=[
        ('PENDIENTE', 'Pendiente'),
        ('EN_CURSO', 'En curso'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
    ])

    class Meta:
        db_table = 'pedido'
        ordering = ['fecha_ingreso']
    
    def clean(self):
        if self.estado_pedido == 'COMPLETADO' and self.lineapedido_set.filter(estado_linea='PENDIENTE').exists():
            raise ValidationError("No se puede completar un pedido con líneas pendientes.")
    
    def __str__(self):
        return f'Pedido {self.numero_pedido} - {self.cliente}'

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    sku_producto = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    fecha_entrega = models.DateField()
    tipo_producto = models.CharField(max_length=3, choices=[('MTO', 'MTO'), ('MTS', 'MTS')])
    
    def clean(self):
        if self.tipo_producto == 'MTO' and self.estado_linea != 'COMPLETADO':
            raise ValidationError("Una línea MTO debe tener estado 'COMPLETADO'.")

class DocumentoEntrega(models.Model):
    linea_pedido = models.ForeignKey(LineaPedido, on_delete=models.CASCADE)
    numero_documento = models.AutoField(primary_key=True)
    fecha_despacho = models.DateField()
    fecha_entrega_cliente = models.DateField()
    estado_linea = models.CharField(max_length=20)  # Pendiente, En proceso, Completado, etc.
    
    def clean(self):
        if self.linea_pedido.estado_linea not in ('EN_CURSO', 'COMPLETADO'):
            raise ValidationError("Solo se puede crear un documento de entrega para una línea en curso o completada.")
        if self.fecha_despacho > self.fecha_entrega_cliente:
            raise ValidationError("La fecha de despacho no puede ser posterior a la fecha de entrega al cliente.")

class GuiaTransporte(models.Model):
    numero_guia = models.AutoField(primary_key=True)
    fecha_despacho = models.DateField()
    cliente_destino = models.CharField(max_length=50)
    destino_guia = models.CharField(max_length=50)
    
    def clean(self):
        if self.fecha_despacho < self.documentoentrega_set.aggregate(Min('fecha_despacho'))['fecha_despacho__min']:
            raise ValidationError("La fecha de despacho de la guía no puede ser anterior a la fecha de despacho de los documentos de entrega asociados.")

class PruebaEntrega(models.Model):
    guia_transporte = models.ForeignKey(GuiaTransporte, on_delete=models.CASCADE)
    foto_guia = models.ImageField(upload_to='fotos_guia/')
    foto_documento_entrega = models.ImageField(upload_to='fotos_documentos/')
    observacion = models.TextField()
    
class Factura(models.Model):
    numero_factura = models.AutoField(primary_key=True)
    documentos_entrega = models.ManyToManyField(DocumentoEntrega)
    fecha_facturacion = models.DateField()
    estado_factura = models.CharField(max_length=20)  # Pendiente, En proceso, Completado, etc.

    def clean(self):
        if self.estado_factura == 'COMPLETADO' and not self.documentos_entrega.filter(estado_linea='COMPLETADO').exists():
            raise ValidationError("No se puede completar una factura sin documentos de entrega completados.")

class RadicacionFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_radicacion = models.DateField()
    metodo_radicacion = models.CharField(max_length=20)  