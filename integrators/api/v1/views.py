from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from integrators import models
from . import serializers
from integrators import repositories


class ContractViewSet(viewsets.ModelViewSet):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    repository = repositories.ContractRepository()

    def create(self, request):
        data = request.data
        response_data = self.repository.create(data)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def list(self, request):
        response_data = self.repository.get_all()
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = models.Contract.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        response_data = self.repository.retrieve(location)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        instance = self.get_object()
        data = request.data
        response_data = self.repository.update(instance, data)
        return Response(response_data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        instance = self.get_object()
        data = request.data
        response_data = self.repository.partial_update(instance, data)
        return Response(response_data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.repository.delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IntegratorViewSet(viewsets.ModelViewSet):
    queryset = models.Integrator.objects.all()
    serializer_class = serializers.IntegratorSerializer
    repository = repositories.IntegratorRepository()

    def create(self, request):
        data = request.data
        response_data = self.repository.create(data)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def list(self, request):
        response_data = self.repository.get_all()
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = models.Integrator.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        response_data = self.repository.retrieve(location)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        instance = self.get_object()
        data = request.data
        response_data = self.repository.update(instance, data)
        return Response(response_data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        instance = self.get_object()
        data = request.data
        response_data = self.repository.partial_update(instance, data)
        return Response(response_data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.repository.delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


