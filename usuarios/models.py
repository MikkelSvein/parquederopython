from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # extend later if needed
    documento = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    is_cliente = models.BooleanField(default=False)
    def __str__(self):
        return self.username
