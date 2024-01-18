from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Configuration(models.Model):
    """Abstract class used by any configuration classes"""
    name = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        error_messages={
            'unique': 'This config already exists'
        }
    )

    class Scope(models.TextChoices):
        UNKNOWN = "UN", _("Unknown")
        MASTERCARD = "MC", _("Mastercard Level 2")
        VISA = "VI", _("Visa Level 2")
        PRODUCTION = "PR", _("Production Level 3")

    scope = models.CharField(
        max_length=2,
        choices=Scope.choices,
        default=Scope.UNKNOWN
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class EMVConfiguration(Configuration):
    """EMV Configuration to process EMV cards"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    value = models.CharField(max_length=1000)







