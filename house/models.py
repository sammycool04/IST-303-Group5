from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length = 30)

    # def __str__(self):
    #     return self.name

class Category(models.Model):
    name = models.CharField(max_length = 20)

    # def __str__(self):
    #     return self.name

class House(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 200)
    # location = models.CharField(max_length = 200)
    # host = models.ForeignKey(Host, on_delete=models.CASCADE)
    # categories = models.ManyToManyField(Category)
    # publish_date = models.DateTimeField(auto_now_add = True)
    # views = models.IntegerField(default=0)
    # reviewed = models.BooleanField(default=False)
    #
    # def __str__(self):
    #     return self.summary
