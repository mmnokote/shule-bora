from rest_framework import serializers
from .models import DataProvider, DataRecord

class DataProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataProvider
        fields = '__all__'

class DataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecord
        fields = '__all__'
