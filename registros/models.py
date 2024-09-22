from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission #AbstractUser es el modelo que tiene el usuario por defecto
from django.core.validators import RegexValidator

# Create your models here.

class CustomUser(AbstractUser):
    edad=models.IntegerField(blank=True, null=True)
    sexo=models.CharField(max_length=10, blank=True, null=True)
    altura=models.IntegerField(blank=True, null=True)
    telefono = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',  # Patrón para un número internacional
            message="El número de teléfono debe ingresarse en el formato: '+999999999'. Hasta 15 dígitos permitidos."
        )]
    )
    #Las siguientes dos líneas quizá estén de más, pero está bien por si acaso
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set", blank=True)
    def __str__(self):
        return self.username