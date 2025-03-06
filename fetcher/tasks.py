import requests
from celery import shared_task
from .models import DataProvider, DataRecord

@shared_task
def fetch_data(provider_id):
    provider = DataProvider.objects.get(id=provider_id)
    
    headers = {}
    if provider.auth_token:
        headers["Authorization"] = f"Bearer {provider.auth_token}"
    
    try:
        response = requests.get(provider.api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        DataRecord.objects.create(provider=provider, raw_data=data)
        return f"Data fetched from {provider.name}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {str(e)}"


@shared_task
def reprocess_data():
    records = DataRecord.objects.filter(status='raw')
    for record in records:
        processed_data = {"processed": record.raw_data}  # Add processing logic here
        record.processed_data = processed_data
        record.status = "processed"
        record.processed_at = timezone.now()
        record.save()
    return f"{records.count()} records processed"
