from rest_framework import routers
from .views import UserViewSet, ZoneViewSet, HistoryViewSet, AlertViewSet, EventViewSet

# create router for the viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'alerts', AlertViewSet)
router.register(r'events', EventViewSet)
