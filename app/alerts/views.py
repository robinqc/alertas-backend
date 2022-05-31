from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Alert, History, PhoneNumber, Zone, Event
from rest_framework.permissions import AllowAny
from .serializers import AlertSerializer, EventSerializer, HistorySerializer, PhoneNumberSerializer, ZoneSerializer, MyTokenObtainPairSerializer


class PhoneNumberViewSet(ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

class ZoneViewSet(ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class AlertViewSet(ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    