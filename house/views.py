from django.shortcuts import render
from .models import HouseInfo
from Worksample.views import house_data

# Create your views here.


def insertData(request):
    data = house_data()

    for dic in data:
        query = HouseInfo(image=dic["image"], address=dic["address"], latitude=dic["latitude"],
                          longitude=dic["longitude"], price=dic["price"], categories=dic["categories"],
                          summary=dic["summary"])
        query.save()

    # pass



