from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import TextField


class Bolim(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Mahsulot(models.Model):
    nom = models.CharField(max_length=255)
    brend = models.CharField(max_length=255, blank=True, null=True)
    narx1 = models.FloatField(validators=[MinValueValidator(0.0)])
    narx2 = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    olchov = models.CharField(max_length=10)
    oxirgi_sana = models.DateTimeField(blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom


class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    dokon = models.CharField(max_length=222)
    tel = models.CharField(max_length=15)
    manzil = models.TextField(blank=True, null=True)
    qarz = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ism
