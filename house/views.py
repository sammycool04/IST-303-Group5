from django.shortcuts import render
from .models import HouseInfo
from Worksample.views import house_data

# Create your views here.

def BootstrapFilterView(request):
    # qs = HouseInfo.objects.all()
    # title_contains_query = request.GET.get("title_contains")
    # if title_contains_query != "" and title_contains_query is not None:
    #     qs = qs.filter(summary__icontains=title_contains_query)
    # return render(request, "bootstrap_form.html", qs)
    return render(request, "bootstrap_form.html", {1: "abc"})

def insertData(request):
    data = house_data()

    for dic in data:
        query = HouseInfo(image=dic["image"], address=dic["address"], latitude=dic["latitude"],
                          longitude=dic["longitude"], price=dic["price"], categories=dic["categories"],
                          summary=dic["summary"])
        query.save()

    # pass



