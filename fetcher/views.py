from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import DataProvider, DataRecord
from .serializers import DataProviderSerializer, DataRecordSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import fetch_data

class DataProviderViewSet(viewsets.ModelViewSet):
    queryset = DataProvider.objects.all()
    serializer_class = DataProviderSerializer

class DataRecordViewSet(viewsets.ModelViewSet):
    queryset = DataRecord.objects.all()
    serializer_class = DataRecordSerializer



@api_view(['POST'])
def trigger_fetch(request, provider_id):
    try:
        provider = DataProvider.objects.get(id=provider_id)
        if provider.fetch_method == 'queue':
            fetch_data.delay(provider.id)
            return Response({"message": "Fetch task added to queue"}, status=202)
        else:
            fetch_data(provider.id)
            return Response({"message": "Data fetched in real-time"}, status=200)
    except DataProvider.DoesNotExist:
        return Response({"error": "Provider not found"}, status=404)


