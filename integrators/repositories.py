from .models import (
    Contract,
    Integrator
)
from .api.v1.serializers import (
    ContractSerializer,
    IntegratorSerializer,
)


class ContractRepository:
    def create(self, data):
        serializer = ContractSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def get_all(self):
        data = Contract.objects.all()
        serializer = ContractSerializer(data, many=True)
        return serializer.data

    def retrieve(self, instance):
        serializer = ContractSerializer(instance)
        return serializer.data

    def update(self, instance, data):
        serializer = ContractSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def partial_update(self, instance, data):
        serializer = ContractSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete(self, instance):
        instance.delete()


class IntegratorRepository:
    def create(self, data):
        serializer = IntegratorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def get_all(self):
        data = Integrator.objects.all()
        serializer = IntegratorSerializer(data, many=True)
        return serializer.data

    def retrieve(self, instance):
        serializer = IntegratorSerializer(instance)
        return serializer.data

    def update(self, instance, data):
        serializer = IntegratorSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def partial_update(self, instance, data):
        serializer = IntegratorSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete(self, instance):
        instance.delete()


