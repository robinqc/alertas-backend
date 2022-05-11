from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)

class Zone(models.Model):
    department = models.CharField(max_length=128)   # DEPARTAMENTO
    municipality = models.CharField(max_length=128) # MUNICIPIO
    village = models.CharField(max_length=128)      # CORREGIMIENTO
    latitude = models.FloatField()                  # LATITUD
    longitude = models.FloatField()                 # LONGITUD

class Event(models.Model):
    description = models.CharField(max_length=256)

class History(models.Model):
    observations = models.CharField(max_length=256)

class Alert(models.Model):
    details = models.CharField(max_length=256)
