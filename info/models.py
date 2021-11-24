from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    max_total_supply = models.IntegerField()
