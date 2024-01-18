from rest_framework import serializers
from switcloud.functions import attempt_json_deserialize
from pops import models 


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Merchant
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = "__all__"


class PointOfPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PointOfPayment
        fields = "__all__"


