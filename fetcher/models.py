from django.db import models

# Create your models here.
class DataProvider(models.Model):
    FETCH_METHODS = [('realtime', 'Real-Time'), ('queue', 'Queue')]
    
    name = models.CharField(max_length=255, unique=True)
    api_url = models.URLField()
    fetch_method = models.CharField(max_length=10, choices=FETCH_METHODS, default='queue')
    auth_token = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DataRecord(models.Model):
    provider = models.ForeignKey(DataProvider, on_delete=models.CASCADE)
    raw_data = models.JSONField()
    processed_data = models.JSONField(blank=True, null=True)
    fetched_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('raw', 'Raw'), ('processed', 'Processed')], default='raw')

    def __str__(self):
        return f"Data from {self.provider.name} at {self.fetched_at}"
