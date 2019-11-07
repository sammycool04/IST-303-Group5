from django.db import models
# from django.contrib.gis.db import models as m

# Create your models here.
# class Host(models.Model):
#     name = models.CharField(max_length = 30)

#     # def __str__(self):
#     #     return self.name

# class Category(models.Model):
#     name = models.CharField(max_length = 20)


class LonLatField(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()

class House(models.Model):
#     # image = models.ImageField(upload_to='images/')
    image = models.URLField()
    summary = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)

    address = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.FloatField()

#     # imageLink = models.URLField(max_length=250)
#     # location = models.ManyToManyField(LonLatField)
#     # categories = models.ManyToManyField(Category)
#     # host = models.ForeignKey(Host, on_delete=models.CASCADE)
#     # publish_date = models.DateTimeField(auto_now_add = True)
#     # views = models.IntegerField(default=0)
#     # reviewed = models.BooleanField(default=False)
#     # def __str__(self):
#     #     return self.summary
    @property
    def is_valid(self):
        return self.price > 0.0



class HouseInfo(models.Model):
    image = models.URLField(default='#')
    address = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='0,0')
    price = models.FloatField(default=0.0)
    categories = models.CharField(max_length=200, default='')
    summary = models.CharField(max_length=200, default='')

    class Meta():
        managed: True
