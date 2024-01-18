from rest_framework import serializers
from switcloud.functions import attempt_json_deserialize
from integrators import models


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contract
        fields = "__all__"


class IntegratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Integrator
        fields = "__all__"


