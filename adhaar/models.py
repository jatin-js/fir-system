from django.db import models

class Usern(models.Model):
    adhaar_number = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=10)
# Create your models here.
