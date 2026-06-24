from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        # producto: alinear nombres y campos con el diccionario de datos
        migrations.RenameField(
            model_name='producto', old_name='precio', new_name='precio_venta',
        ),
        migrations.RenameField(
            model_name='producto', old_name='stock', new_name='stock_actual',
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_minimo',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        # compra: fecha -> fecha_compra y numero_factura
        migrations.RenameField(
            model_name='compra', old_name='fecha', new_name='fecha_compra',
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_factura',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterModelOptions(
            name='compra',
            options={
                'ordering': ['-fecha_compra'],
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        # proveedor: longitud de nombre segun diseno
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
        # pago: tipos segun diseno
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pago',
            name='metodo_pago',
            field=models.CharField(
                choices=[
                    ('efectivo', 'Efectivo'),
                    ('tarjeta', 'Tarjeta'),
                    ('transferencia', 'Transferencia'),
                    ('otro', 'Otro'),
                ],
                default='efectivo',
                max_length=50,
            ),
        ),
    ]
