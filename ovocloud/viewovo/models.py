from django.db import models

class Viewovo(models.Model):
    id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description', null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        fila = "Title: " + self.tittle + " Description: " + self.description
        return fila

    # Eliminar imagen del sistema al eliminar el registro
    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.storage.delete(self.image.name)
        super().delete(using=using, keep_parents=keep_parents)


class MonitoreoAgua(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    sitio_toma = models.CharField(max_length=255, verbose_name="Sitio de Toma")
    ph = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="pH (6.5 a 9.0)")
    cloro_residual = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Cloro Residual (ppm)")
    dureza = models.IntegerField(verbose_name="Dureza (ppm < 250)")
    adicion_cloro = models.IntegerField(verbose_name="Adición Cloro Cantidad (Un)", null=True, blank=True)
    vigencia_reactivos = models.CharField(max_length=255, verbose_name="Vigencia de Reactivos", null=True, blank=True)
    responsable = models.CharField(max_length=255, verbose_name="Responsable")
    observaciones = models.TextField(verbose_name="Observaciones", null=True, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.sitio_toma}"


class RegistroViaje(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    dia = models.CharField(max_length=10, verbose_name="Día")
    placa = models.CharField(max_length=10, verbose_name="Placa")
    conductor = models.CharField(max_length=100, verbose_name="Conductor")
    ruta = models.CharField(max_length=255, verbose_name="Ruta")
    mp_pt = models.CharField(max_length=2, verbose_name="MP/PT")
    kilos = models.PositiveIntegerField(null=True, blank=True, verbose_name="Kilos")
    km_inicial = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Km Inicial")
    km_final = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Km Final")
    km = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="KM")
    gal_acpm = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Gal ACPM")
    valor_acpm = models.CharField(max_length=20, null=True, blank=True, verbose_name="$ ACPM")
    cant_peajes = models.PositiveIntegerField(null=True, blank=True, verbose_name="Cant Peajes")
    valor_peajes = models.CharField(max_length=20, null=True, blank=True, verbose_name="Valor Peajes")
    viaticos = models.CharField(max_length=20, null=True, blank=True, verbose_name="$ Viáticos")
    otros = models.CharField(max_length=20, null=True, blank=True, verbose_name="$ Otros")
    valor_kg = models.CharField(max_length=10, null=True, blank=True, verbose_name="Vr. / Kg")
    consignacion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Consignación")
    pago_con_tesoreria = models.CharField(max_length=255, null=True, blank=True, verbose_name="Pago conciliado con tesorería")

    def __str__(self):
        return f"{self.fecha} - {self.placa} - {self.conductor}"
