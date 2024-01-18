from rest_framework import serializers
from switcloud.functions import attempt_json_deserialize
from configurations import models


class EMVConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EMVConfiguration
        fields = "__all__"

