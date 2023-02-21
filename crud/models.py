from django.db import models
from django.contrib.auth.models import User




 

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes/',null=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)    

    def __str__(self) -> str:
        return self.imagen