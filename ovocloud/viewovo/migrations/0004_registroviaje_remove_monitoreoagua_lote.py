# Generated by Django 5.1.7 on 2025-06-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewovo', '0003_monitoreoagua_lote'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroViaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('dia', models.CharField(max_length=10, verbose_name='Día')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('conductor', models.CharField(max_length=100, verbose_name='Conductor')),
                ('ruta', models.CharField(max_length=255, verbose_name='Ruta')),
                ('mp_pt', models.CharField(max_length=2, verbose_name='MP/PT')),
                ('kilos', models.PositiveIntegerField(blank=True, null=True, verbose_name='Kilos')),
                ('km_inicial', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Km Inicial')),
                ('km_final', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Km Final')),
                ('km', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='KM')),
                ('gal_acpm', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Gal ACPM')),
                ('valor_acpm', models.CharField(blank=True, max_length=20, null=True, verbose_name='$ ACPM')),
                ('cant_peajes', models.PositiveIntegerField(blank=True, null=True, verbose_name='Cant Peajes')),
                ('valor_peajes', models.CharField(blank=True, max_length=20, null=True, verbose_name='Valor Peajes')),
                ('viaticos', models.CharField(blank=True, max_length=20, null=True, verbose_name='$ Viáticos')),
                ('otros', models.CharField(blank=True, max_length=20, null=True, verbose_name='$ Otros')),
                ('valor_kg', models.CharField(blank=True, max_length=10, null=True, verbose_name='Vr. / Kg')),
                ('consignacion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Consignación')),
                ('pago_con_tesoreria', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pago conciliado con tesorería')),
            ],
        ),
        migrations.RemoveField(
            model_name='monitoreoagua',
            name='lote',
        ),
    ]
