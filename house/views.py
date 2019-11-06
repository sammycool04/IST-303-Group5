from django.shortcuts import render
from .models import House

from .models import HouseInfo

# Create your views here.
# def house(request):
#     house = House.objects
#     return render(request, 'house/home.html', {'house': house})

def BootstrapFilterView(request):
    qs = House.objects.all()
    # title_exact_query = request.GET.get('title_exact')
    # title_or_author_query = request.GET.get('title_or_author')
    # print(title_contains)

    # qs = HouseInfo.objects.all()
    title_contains_query = request.GET.get('title_contains')

    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(summary__icontains=title_contains_query)
    context = {
        'queryset': qs
    }
    # return render(request, 'bootstrap_form.html',context)
    return render(request, 'bootstrap_form.html', {1:"abc"})
    # return render(request, 'searchByAdd.html', {})


