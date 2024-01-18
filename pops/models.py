from django.db import models
from integrators.models import Integrator


class Merchant(models.Model):
    integrator = models.ForeignKey(
        Integrator,
        on_delete=models.CASCADE,
        related_name="merchants")
    name = models.CharField(max_length=50)
    """Refer to ISO merchant category codes"""
    category_code = models.PositiveSmallIntegerField(blank=False, name='MCC', default=0)

    def __str__(self):
        return self.name    


class Location(models.Model):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        related_name="locations")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name    


class PointOfPayment(models.Model):
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="pops")
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    terminal_id = models.CharField(max_length=16)    
    brand = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.brand, self.name)
