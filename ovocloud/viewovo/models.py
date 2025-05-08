from django.db import models

# Create your models here.
class Viewovo(models.Model):
    id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description', null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        fila = "Title: " + self.tittle + " Description: " + self.description
        return fila
    #Modelo para eliminar la imagen de la base de datos y el archivo en el servidor
    def delete(self, using=None, keep_parents=False,):
        self.image.storage.delete(self.image.name)
        super().delete()
        
        
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
    