from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Contract(models.Model):
    """Contract establishing business relation between switstack and integrator"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class ContractType(models.TextChoices):
        UNKNOWN = "UN", _("Unknown")
        PSP = "PP", _("Payment Service Provider")
        MERCHANT = "MC", _("Merchant")
        PROCESSOR = "PR", _("Processor")

    integrator_type = models.CharField(
        max_length=2,
        choices=ContractType.choices,
        default=ContractType.UNKNOWN
    )
    reference = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=250)
    owner = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    is_signed = models.BooleanField(default=False) 

    def __str__(self):
        return self.reference


class Integrator(models.Model):
    """Model to manage the PSP a-like role, i.e a switcloud customer"""
    contract = models.OneToOneField(
        Contract,
        on_delete=models.SET_NULL,
        related_name="signee",
        null=True
    )    
    company_name = models.CharField(max_length=50,blank=True)
    company_address = models.CharField(max_length=500, blank=True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=250, blank=True, unique=True)
    contact_phone_1 = models.CharField(max_length=50, blank=True)
    contact_phone_2 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.company_name


