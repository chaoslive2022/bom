from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from pops import models
from . import serializers
from pops import repositories


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = models.Merchant.objects.all()
    serializer_class = serializers.MerchantSerializer
    repository = repositories.MerchantRepository()

    def create(self, request):
        data = request.data
        response_data = self.repository.create(data)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def list(self, request):
        response_data = self.repository.get_all()
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = models.Merchant.objects.all()
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


class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    repository = repositories.LocationRepository()

    def create(self, request):
        data = request.data
        response_data = self.repository.create(data)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def list(self, request):
        response_data = self.repository.get_all()
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = models.Location.objects.all()
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


class PointOfPaymentViewSet(viewsets.ModelViewSet):
    queryset = models.PointOfPayment.objects.all()
    serializer_class = serializers.PointOfPaymentSerializer
    repository = repositories.PointOfPaymentRepository()

    def create(self, request):
        data = request.data
        response_data = self.repository.create(data)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def list(self, request):
        response_data = self.repository.get_all()
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = models.PointOfPayment.objects.all()
        pop = get_object_or_404(queryset, pk=pk)
        response_data = self.repository.retrieve(pop)
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


