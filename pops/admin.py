from django.contrib import admin
from pops import models

# Register your models here.
admin.site.register(models.Merchant)
admin.site.register(models.Location)
admin.site.register(models.PointOfPayment)
