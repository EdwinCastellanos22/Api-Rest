from django.db import models

# Create your models here.
class Usuario(models.Model):

    id= models.AutoField(primary_key=True)
    Nombre= models.CharField(max_length=50)
    url= models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre, self.url