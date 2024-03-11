# Generated by Django 5.0.3 on 2024-03-11 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoEntrega',
            fields=[
                ('numero_documento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_despacho', models.DateField()),
                ('fecha_entrega_cliente', models.DateField()),
                ('estado_linea', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaTransporte',
            fields=[
                ('numero_guia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_despacho', models.DateField()),
                ('cliente_destino', models.CharField(max_length=50)),
                ('destino_guia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LineaPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_producto', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('fecha_entrega', models.DateField()),
                ('tipo_producto', models.CharField(choices=[('MTO', 'MTO'), ('MTS', 'MTS')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('numero_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateField()),
                ('cliente', models.CharField(max_length=100)),
                ('estado_pedido', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('EN_CURSO', 'En curso'), ('COMPLETADO', 'Completado'), ('CANCELADO', 'Cancelado')], max_length=20)),
            ],
            options={
                'db_table': 'pedido',
                'ordering': ['fecha_ingreso'],
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_facturacion', models.DateField()),
                ('estado_factura', models.CharField(max_length=20)),
                ('documentos_entrega', models.ManyToManyField(to='logistica_api.documentoentrega')),
            ],
        ),
        migrations.AddField(
            model_name='documentoentrega',
            name='linea_pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistica_api.lineapedido'),
        ),
        migrations.AddField(
            model_name='lineapedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistica_api.pedido'),
        ),
        migrations.CreateModel(
            name='PruebaEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_guia', models.ImageField(upload_to='fotos_guia/')),
                ('foto_documento_entrega', models.ImageField(upload_to='fotos_documentos/')),
                ('observacion', models.TextField()),
                ('guia_transporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistica_api.guiatransporte')),
            ],
        ),
        migrations.CreateModel(
            name='RadicacionFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_radicacion', models.DateField()),
                ('metodo_radicacion', models.CharField(max_length=20)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistica_api.factura')),
            ],
        ),
    ]
