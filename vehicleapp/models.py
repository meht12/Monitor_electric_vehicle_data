from django.db import models

class vehicle(models.Model):
    License_plate = models.CharField(max_length=100)
    make=models.CharField(max_length=100)
    vin=models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    creation_date=models.DateTimeField(auto_now_add=True)
    miles_driven= models.IntegerField(max_length=15)

def __str__(self):
        return self.License_plate
    # CREATE TABLE "vehicleapp_vehicle" (
# 	"id"	integer NOT NULL,
# 	"License_plate"	varchar(100) NOT NULL,
# 	"make"	varchar(100) NOT NULL,
# 	"vin"	varchar(100) NOT NULL,
# 	"model"	varchar(100) NOT NULL,
# 	"types"	varchar(100) NOT NULL,
# 	"creation_date"	datetime NOT NULL,
# 	"miles_driven"	varchar(100) NOT NULL,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# # );