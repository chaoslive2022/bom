from .models import (
    EMVConfiguration
)
from .api.v1.serializers import (
    EMVConfigurationSerializer
)


class EMVConfigurationRepository:
    def create(self, data):
        serializer = EMVConfigurationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def get_all(self):
        data = EMVConfiguration.objects.all()
        serializer = EMVConfigurationSerializer(data, many=True)
        return serializer.data

    def retrieve(self, instance):
        serializer = EMVConfigurationSerializer(instance)
        return serializer.data

    def update(self, instance, data):
        serializer = EMVConfigurationSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def partial_update(self, instance, data):
        serializer = EMVConfigurationSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete(self, instance):
        instance.delete()
