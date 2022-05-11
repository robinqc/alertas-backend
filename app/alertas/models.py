from django.db.models import Model, Charfield, IntegerField
# import django models
class User(models.Model):
    # define fields
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)

class Zone(models.Model):
    department = models.CharField(max_length=64)
    municipality = models.CharField(max_length=64)
