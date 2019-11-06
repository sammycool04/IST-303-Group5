from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# from django.utils import simplejson
# from .forms import NameForm

import operator


def homepage(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


def searchByAdd(request):
    return render(request, 'searchByAdd.html')


def searchByPre(request):
    return render(request, 'searchByPre.html')


#
def getForm(request):
    reqDict = request.GET.dict()
    # reqDict = request.GET.get('')
    print(reqDict)

    return render(request, 'searchByAdd.html', {'d1': 'abcde'})


def searchByPreResult(request):
    pass


def searchByAddResult(request):
    rec = request.GET.get('sa')
    if rec:
        data = house_data()
        retDic = []
        for dic in data:
            if rec in dic['address'].lower().strip():
                retDic.append(dic)
        return JsonResponse(retDic, safe=False)

        # if rec.lower().strip() == 'claremont':
        #     return house_data()
    return JsonResponse([], safe=False)

    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/thanks/')
    #
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     return render(request, 'searchByAdd.html', {})

    # responseData = { 'id': 4, 'name': 'Test Response', 'roles': ['Admin', 'User']}
    # return JsonResponse(responseData)
    # return render(request, 'searchByAdd.html', {'form': ""})

    # ret = house_data()
    # return ret

    # return HttpResponse(request.GET.items())


def house_data():
    houseData = [
        {
            "id": 1,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/IS7uq68u3lahf81000000000.webp",
            "address": "1428 Oxford Ave, Claremont, CA 91711",
            "location": "0.0,0.0",
            "price": 850000,
            "categories": "sale",
            "summary": "Beautifully renovated light and bright 6 bedroom 3 bathroom home. Features include gleaming new kitchen with new white cabinets, quartz countertops, and stainless steel appliances. Couple that with sparkling new bathrooms, recessed lighting, laminate wood floors, two car garage and large lot and this is the ideal place to call home."
        },
        {
            "id": 2,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/ISr1amln7zh79z0000000000.webp",
            "address": "3419 Campus Ave, Claremont, CA 91711",
            "location": "0.0,0.0",
            "price": 589500,
            "categories": "sale",
            "summary": "The updated kitchen with granite counters and stainless-steel appliances offers room for a kitchen table, or additional counter space and storage."
        },
        {
            "id": 3,
            "image": "https://photos.zillowstatic.com/fp/b519e881de2c699c1166a62686fa1d6f-cc_ft_1536.webp",
            "address": "1268 Hillsdale Dr, Claremont, CA 91711",
            "location": "0.0,0.0",
            "price": 665000,
            "categories": "sale",
            "summary": "Well maintained Single family home located in the heart of Claremont. This Beautiful 1 Story Home features 4 BEDROOMS and 2 BATHS. 2,010 Living SF. and 11,725 sf. Lot Size"
        },
        {
            "id": 4,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/ISbdw6gxabi1o61000000000.webp",
            "address": "118 Bloom Dr, Claremont, CA 91711",
            "location": "0.0,0.0",
            "price": 464000,
            "categories": "sale",
            "summary": "Investor and homebuyer opportunity! This property is being offered at a live auction on 01-02-2020. Buy it as an investment or enjoy it as your own home."
        },
        {
            "id": 5,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/IS7azz04x1ojsn1000000000.webp",
            "address": "214 E College Way, Claremont, CA 91711",
            "location": "0.0,0.0",
            "price": 684900,
            "categories": "sale",
            "summary": "If you are looking for that perfect Mid-Century home, this is the one you have been waiting for. Don't miss this opportunity to own a home located in the Piedmont Mesa area! This home has an original mural from the prestigious Henderson builder. "
        },
        {
            "id": 6,
            "image": "https://photos.zillowstatic.com/fp/c9d6a3aebdb81f21577805327b5fc251-cc_ft_1536.webp",
            "address": "2531 N Mountain Ave, Claremont, CA 91711",
            "location": "0.0,0.0",
            "price": 1080000,
            "categories": "sale",
            "summary": "This custom built mid century modern home, located in the prestigious hillside community of Claraboya, truly has everything for today's discerning buyer. "
        }
    ]

    # return JsonResponse(houseData, safe=False)
    return houseData


if __name__ == '__main__':
    dsa = house_data()
    for di in dsa:
        print('claremont' in di['address'].lower())
