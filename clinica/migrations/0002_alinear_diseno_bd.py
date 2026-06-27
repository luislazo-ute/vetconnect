import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
        ('pacientes', '0002_cita_historialmedico'),
    ]

    operations = [
        # vacuna
        migrations.RenameField(
            model_name='vacuna', old_name='nombre', new_name='nombre_vacuna',
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='nombre_vacuna',
            field=models.CharField(max_length=100),
        ),
        migrations.RenameField(
            model_name='vacuna', old_name='fecha_proxima', new_name='fecha_proxima_dosis',
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='lote',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        # habitacion
        migrations.RenameField(
            model_name='habitacion', old_name='numero', new_name='codigo',
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='codigo',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='tipo',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        # hospitalizacion
        migrations.RenameField(
            model_name='hospitalizacion', old_name='fecha_salida', new_name='fecha_alta',
        ),
        # receta
        migrations.AddField(
            model_name='receta',
            name='cita',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='recetas', to='pacientes.cita',
            ),
        ),
        migrations.RenameField(
            model_name='receta', old_name='fecha', new_name='fecha_emision',
        ),
        migrations.AlterField(
            model_name='receta',
            name='fecha_emision',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='receta',
            name='valida_hasta',
            field=models.DateField(blank=True, null=True),
        ),
        # detalle_receta
        migrations.RemoveField(model_name='detallereceta', name='duracion'),
        migrations.AddField(
            model_name='detallereceta',
            name='duracion_dias',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallereceta',
            name='dosis',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detallereceta',
            name='frecuencia',
            field=models.CharField(max_length=100),
        ),
        # notificacion
        migrations.AlterField(
            model_name='notificacion',
            name='tipo',
            field=models.CharField(
                choices=[
                    ('recordatorio', 'Recordatorio'),
                    ('alerta', 'Alerta'),
                    ('informacion', 'Información'),
                ],
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='titulo',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
