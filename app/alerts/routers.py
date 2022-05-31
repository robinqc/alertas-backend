from rest_framework import routers
from .views import PhoneNumberViewSet, ZoneViewSet, HistoryViewSet, AlertViewSet, EventViewSet

# create router for the viewsets
router = routers.DefaultRouter()
router.register(r'phones', PhoneNumberViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'alerts', AlertViewSet)
router.register(r'events', EventViewSet)
