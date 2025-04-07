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