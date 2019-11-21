from django.db import models
# from django.contrib.gis.db import models as m
# import Worksample.views

# Create your models here.

class HouseInfo(models.Model):
    image = models.URLField(default="#")
    address = models.CharField(max_length=200, default="")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    categories = models.CharField(max_length=200, default="")
    summary = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.address.split(',')[0]

    class Meta():
        managed: True




