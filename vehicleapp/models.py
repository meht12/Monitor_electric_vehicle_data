from django.db import models

class vehicle(models.Model):
    License_plate = models.CharField(max_length=100)
    make=models.CharField(max_length=100)
    vin=models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    creation_date=models.DateTimeField(auto_now_add=True)
    miles_driven= models.TextField(max_length=15)

    
