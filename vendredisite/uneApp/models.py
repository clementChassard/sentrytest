# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class client(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_nat = models.DateField(blank=False, verbose_name="date de naissance")
    email = models.EmailField(blank=False, verbose_name="votre email:")

    def __str__(self):
        return self.nom

