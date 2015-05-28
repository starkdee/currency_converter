from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, blank=False)
    full_name = models.CharField(max_length=100, blank=False)

class Rate(models.Model):
    currency = models.ForeignKey(Currency)

    rate = models.FloatField(blank=False)