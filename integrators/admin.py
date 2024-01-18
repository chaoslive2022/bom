from django.contrib import admin
from integrators import models

# Register your models here.
admin.site.register(models.Integrator)
admin.site.register(models.Contract)