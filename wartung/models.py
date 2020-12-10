from django.conf import settings
from django.db import models
from django.utils import timezone

class Locus(models.Model):
    plz = models.CharField(max_length=8)
    ort = models.CharField(max_length=35)
    landkreis = models.CharField(max_length=45, null=True)
    bundesland = models.CharField(max_length=25)

    class Meta:
        ordering = ['bundesland', 'ort']

    def __str__(self):
        return f'{self.plz}, {self.ort}, {self.bundesland}'


