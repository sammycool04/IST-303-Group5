from django.shortcuts import render

from .models import House

# Create your views here.
def house(request):
    house = House.objects
    return render(request, 'house/home.html', {'house': house})