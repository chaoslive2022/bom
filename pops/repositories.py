from .models import (
    Merchant,
    Location,
    PointOfPayment
)
from .api.v1.serializers import (
    MerchantSerializer,
    LocationSerializer,
    PointOfPaymentSerializer
)

class MerchantRepository:
    def create(self, data):
        serializer = MerchantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def get_all(self):
        data = Merchant.objects.all()
        serializer = MerchantSerializer(data, many=True)
        return serializer.data

    def retrieve(self, instance):
        serializer = MerchantSerializer(instance)
        return serializer.data

    def update(self, instance, data):
        serializer = MerchantSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def partial_update(self, instance, data):
        serializer = MerchantSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete(self, instance):
        instance.delete()


class LocationRepository:
    def create(self, data):
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def get_all(self):
        data = Location.objects.all()
        serializer = LocationSerializer(data, many=True)
        return serializer.data

    def retrieve(self, instance):
        serializer = LocationSerializer(instance)
        return serializer.data

    def update(self, instance, data):
        serializer = LocationSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def partial_update(self, instance, data):
        serializer = LocationSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete(self, instance):
        instance.delete()


class PointOfPaymentRepository:
    def create(self, data):
        serializer = PointOfPaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def get_all(self):
        data = PointOfPayment.objects.all()
        serializer = PointOfPaymentSerializer(data, many=True)
        return serializer.data

    def retrieve(self, instance):
        serializer = PointOfPaymentSerializer(instance)
        return serializer.data

    def update(self, instance, data):
        serializer = PointOfPaymentSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def partial_update(self, instance, data):
        serializer = PointOfPaymentSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete(self, instance):
        instance.delete()