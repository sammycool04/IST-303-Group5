from django.db import models
# from django.contrib.gis.db import models as m
# import Worksample.views

# Create your models here.
# class Host(models.Model):
#     name = models.CharField(max_length = 30)

#     # def __str__(self):
#     #     return self.name

# class Category(models.Model):
#     name = models.CharField(max_length = 20)


# class LonLatField(models.Model):
#     lon = models.FloatField()
#     lat = models.FloatField()

class House(models.Model):
#     # image = models.ImageField(upload_to='images/')
    image = models.URLField()
    summary = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)

    address = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.FloatField()


#     # def __str__(self):
#     #     return self.summary



class HouseInfo(models.Model):
    image = models.URLField(default="#")
    address = models.CharField(max_length=200, default="")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    room = models.IntegerField(default=1)
    bath = models.IntegerField(default=1)
    size = models.IntegerField(default=0)
    categories = models.CharField(max_length=200, default="")
    summary = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.address.split(',')[0]

    class Meta():
        managed: True

