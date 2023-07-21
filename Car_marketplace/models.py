from django.db import models
from django.contrib.auth.models import User

CAR_BRAND = (
    ('volkswagen', 'Volkswagen'),
    ('skoda', 'Skoda'),
    ('audi', 'Audi'),
    ('bmw', 'Bmw'),
    ('mercedes', 'Mercedes'),
    ('tesla', 'Tesla')
)

STARE = (
    (0, 'Indisponibil'),
    (1, 'Disponibil')
)

class Item(models.Model):
    masina = models.CharField(max_length=1000, unique=True)
    descriere = models.CharField(max_length=2000)
    pret = models.DecimalField(max_digits=10, decimal_places=3)
    marca_masina = models.CharField(max_length=200, choices=CAR_BRAND)
    autor = models.ForeignKey(User, on_delete=models.PROTECT) # foloseste o cheie externa, care e setata ca cel care pune anuntul sa nu poata fi sters
    stare = models.IntegerField(choices=STARE, default=1)
    data_crearii = models.DateTimeField(auto_now_add=True)
    data_actualizarii = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.masina
