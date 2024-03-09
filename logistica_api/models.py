from django.db import models

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField()
    cliente = models.CharField(max_length=100)
    # Otros campos según sea necesario

    class Meta:
        db_table = 'pedido'
        ordering = ['fecha_ingreso']

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    sku_producto = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    fecha_entrega = models.DateField()
    tipo_producto = models.CharField(max_length=3, choices=[('MTO', 'MTO'), ('MTS', 'MTS')])
    # Otros campos según sea necesario

class DocumentoEntrega(models.Model):
    linea_pedido = models.ForeignKey(LineaPedido, on_delete=models.CASCADE)
    numero_documento = models.AutoField(primary_key=True)
    fecha_despacho = models.DateField()
    fecha_entrega_cliente = models.DateField()
    estado_linea = models.CharField(max_length=20)  # Pendiente, En proceso, Completado, etc.
    # Otros campos según sea necesario

class GuiaTransporte(models.Model):
    numero_guia = models.AutoField(primary_key=True)
    fecha_despacho = models.DateField()
    cliente_destino = models.CharField(max_length=50)
    destino_guia = models.CharField(max_length=50)
    # Otros campos según sea necesario

class PruebaEntrega(models.Model):
    guia_transporte = models.ForeignKey(GuiaTransporte, on_delete=models.CASCADE)
    foto_guia = models.ImageField(upload_to='fotos_guia/')
    foto_documento_entrega = models.ImageField(upload_to='fotos_documentos/')
    observacion = models.TextField()
    # Otros campos según sea necesario

class Factura(models.Model):
    numero_factura = models.AutoField(primary_key=True)
    documentos_entrega = models.ManyToManyField(DocumentoEntrega)
    fecha_facturacion = models.DateField()
    estado_factura = models.CharField(max_length=20)  # Pendiente, En proceso, Completado, etc.
    # Otros campos según sea necesario

class RadicacionFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_radicacion = models.DateField()
    metodo_radicacion = models.CharField(max_length=20)  # Email o Mensajeria
    # Otros campos según sea necesario