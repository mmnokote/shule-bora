from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataProviderViewSet, DataRecordViewSet
from .views import trigger_fetch

router = DefaultRouter()
router.register(r'providers', DataProviderViewSet)
router.register(r'records', DataRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fetch-data/<int:provider_id>/', trigger_fetch, name='fetch-data'),

]
