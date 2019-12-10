from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
# from django.utils import simplejson
from .forms import NameForm
from house.models import HouseInfo
import operator
from django.contrib.auth.models import User
from django.contrib import auth


def homepage(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('homepg')
        else:
            return render(request, 'account/signup.html', {'error':'password must match'})

    else:
        return render(request,'account/signup.html')

def signin(request):
    if request.method == 'POST':
        auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('homepg')
        else:
            return render(request,'account/login.html',{'error': 'username or password is not correct.'})
    else:
        return render(request,'account/signin.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signin.html')

def searchByAdd(request):
    return render(request, 'searchByAdd.html')

def searchByPre(request):
    return render(request, 'searchByPre.html')

def houseDetail(request):
    return render(request, 'houseDetail.html')


def showMap(request):
    return render(request, 'map.html')

def survey(request):
    return render(request, 'survey.html')

def zillow(request):
    return render(request, 'zillow.html')






def getForm(request):
    reqDict = request.GET.dict()
    print(reqDict)

    return render(request, 'searchByAdd.html', {'d1': 'abcde'})



def searchById(request):
    hId = request.GET.get('id')
    # return JsonResponse([hId], safe=False)

    if hId:
        data = house_data()
        for dic in data:
            if int(hId) == dic['id']:
                return JsonResponse(dic, safe=False)
    return JsonResponse([], safe=False)



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
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISjfrml52t5asw1000000000.webp",
            "address": "613 W Melrose St # 3, Chicago, IL 60657",
            "longitude": "-87.644830",
            "latitude": "41.941040",
            "price": 250000,
            "room": 1,
            "bath": 1,
            "size": 900,
            "categories": "sale",
            "summary": "Spacious 1 bedroom, 1 bath condo sits in the heart of East Lakeview.Blocks to beach, lakefront trail, Red/Brown line, Lake Shore Drive, shopping and dining. "
        },
        {
            "id": 2,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISfkooz2i4snkw1000000000.webp",
            "address": "2718 W Monroe St, Chicago, IL 60612",
            "longitude": "-87.694580",
            "latitude": "41.880270",
            "price": 99000,
            "room": 4,
            "bath": 2,
            "size": 1177,
            "categories": "sale",
            "summary": "This is a 4 bedroom, 2.0 bathroom, multi family home. It is located at 2718 W Monroe St Chicago, Illinois."
        },
        {
            "id": 3,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISb561wi86pj081000000000.webp",
            "address": "16500 Fulton Ter, Tinley Park, IL 60477",
            "longitude": "-87.766610",
            "latitude": "41.591820",
            "price": 389900,
            "room": 5,
            "bath": 3,
            "size": 2900,
            "categories": "sale",
            "summary": "COME SEE THIS BRAND NEW REHABBED PROPERTY IN ALL IT'S GLORY. ARCHITECTURAL TOUCHES AND STUNNING AMOUNTS OF NATURAL LIGHT ABOUND. RELAX IN FRONT OF THE FIREPLACE, OR HAVE A BEVERAGE IN THE THREE SEASONS ENCLOSED PORCH. "
        },
        {
            "id": 4,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISzz93wuhtlchw1000000000.webp",
            "address": "616 N Ashbury Ave, Bolingbrook, IL 60440",
            "longitude": "-88.054800",
            "latitude": "41.720080",
            "price": 264900,
            "room": 3,
            "bath": 2,
            "size": 1587,
            "categories": "sale",
            "summary": "Nothing like it on the market -- Open floor plan renovated Ranch home with Huge Bonus Family Room and Huge clean and ready to be finished full basement which will DOUBLE the size of this home. "
        },
        {
            "id": 5,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISbpt8xht5rqvt0000000000.webp",
            "address": "7329 S Honore St, Chicago, IL 60636",
            "longitude": "-87.669280",
            "latitude": "41.760260",
            "price": 75000,
            "room": 4,
            "bath": 1,
            "size": 1020,
            "categories": "sale",
            "summary": "Well kept raised ranch that features 4bd, 1bt, with finished basement on quiet street."
        },
        {
            "id": 6,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISzngw96216q6b0000000000.webp",
            "address": "618 N Victoria Dr, Palatine, IL 60074",
            "longitude": "-88.007600",
            "latitude": "42.120250",
            "price": 450000,
            "room": 4,
            "bath": 3,
            "size": 2369,
            "categories": "sale",
            "summary": "Many stunning updates throughout this 4 Bedroom, 2.5 Bath home in the sought-after Heatherstone Subdivision. Enjoy neighborhood walking paths, parks/playgrounds, and a scenic pond setting just minutes to downtown Palatine, Metra and highway. Nothing to do but move-in and enjoy!  "
        },
        {
            "id": 7,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISfseyqx8itg3d1000000000.webp",
            "address": "120 Marquette St, Park Forest, IL 60466",
            "longitude": "-87.684470",
            "latitude": "41.476300",
            "price": 59000,
            "room": 2,
            "bath": 1,
            "size": 949,
            "categories": "sale",
            "summary": "THIS SINGLE FAMILY, DETACHED HOUSE HAS 2 NICE SIZED BEDROOMS AND 1 BATHROOM. TO TRANSPORTATION AND SHOPPING. GREAT LOCATION! INVESTORS: DON'T MISS THIS OPPORTUNITY - GREAT RENTAL PROPERTY."
        },
        {
            "id": 8,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/IS7yp0q0uv3fog1000000000.webp",
            "address": "115 Chestnut Hills Cir, Burr Ridge, IL 60527",
            "longitude": "-87.927980",
            "latitude": "41.757490",
            "price": 409000,
            "room": 3,
            "bath": 4,
            "size": 1364,
            "categories": "sale",
            "summary": "Saved the best for the last! Spacious and sunny 3 bedroom, 2 full, and 2 half bath, largest end-unit townhome. Over 1785 square feet plus full finished basement with additional half bath."
        },
        {
            "id": 9,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISrxevoqm2qxz21000000000.webp",
            "address": "3132 S Racine Ave, Chicago, IL 60608",
            "longitude": "-87.656240",
            "latitude": "41.836880",
            "price": 225000,
            "room": 4,
            "bath": 2,
            "size": 1572,
            "categories": "sale",
            "summary": "Investors/developer special in desirable Bridgeport neighborhood. Legal 2 unit in need of renovation. 1st floor demo begun with some framing and new furnace. Excellent opportunity minutes from restaurants, shopping, art galleries, orange line and I55."
        },
        {
            "id": 10,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISf8nbru4tfpb50000000000.webp",
            "address": "252 Bartram Rd, Riverside, IL 60546",
            "longitude": "-87.819080",
            "latitude": "41.835740",
            "price": 345000,
            "room": 3,
            "bath": 2,
            "size": 1424,
            "categories": "sale",
            "summary": "Welcome Home! Make sure to visit this updated and well maintained home in an ideal Riverside location. Lots to offer with so much charm, plenty of light throughout."
        },
        {
            "id": 11,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISr1mf8qrm3apb0000000000.webp",
            "address": "529 Newberry Ave, La Grange Park, IL 60526",
            "longitude": "-87.861950",
            "latitude": "41.824740",
            "price": 255000,
            "room": 3,
            "bath": 1,
            "size": 1411,
            "categories": "sale",
            "summary": "Great opportunity to own in this quiet neighborhood. Tree-lined streets, near parks and schools. Make this home your own! "
        },
        {
            "id": 12,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISv0kwoqhi8rjz0000000000.webp",
            "address": "3403 Grand Blvd, Brookfield, IL 60513",
            "longitude": "-87.853300",
            "latitude": "41.829140",
            "price": 265000,
            "room": 3,
            "bath": 1,
            "size": 1130,
            "categories": "sale",
            "summary": "Perfect for downsizing or starting off! NO steps!! Newer granite counter tops & oak cabinets. Hardwood floors in living room. Newer carpet over hardwood in all Bedrooms. Updated bath. Large utility room. Patio. Fenced yard. 2 car garage."
        },
        {
            "id": 13,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3jr020n5eldh1000000000.webp",
            "address": "4143 Grove Ave, Brookfield, IL 60513",
            "longitude": "-87.841080",
            "latitude": "41.815070",
            "price": 299900,
            "room": 4,
            "bath": 3,
            "size": 1400,
            "categories": "sale",
            "summary": "WOW! Beautiful 4 bed 3 bath home on a nice street of Brookfield. Brand new rehab with amazing finishes. Gorgeous kitchen with tall modern white cabinetry, quartz countertops and stainless steel appliances."
        },
        {
            "id": 14,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS625r7xu3ru4h0000000000.webp",
            "address": "8730 45th St, Lyons, IL 60534",
            "longitude": "-87.839250",
            "latitude": "41.809860",
            "price": 155000,
            "room": 3,
            "bath": 1,
            "size": 918,
            "categories": "sale",
            "summary": "Beautiful patio, long drive way schedule your appointments and write up an offer."
        },
        {
            "id": 15,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISjvnmnpqv7egv1000000000.webp",
            "address": "8546 45th St, Lyons, IL 60534",
            "longitude": "-87.835000",
            "latitude": "41.809900",
            "price": 164000,
            "room": 3,
            "bath": 2,
            "size": 1000,
            "categories": "sale",
            "summary": "CHEAPER THAN RENT!! ORIGINAL OWNER HAVE MAINTAINED AND UPDATED THIS HOME! EXPANDED KITCHEN WITH LOADS OF CABINETS AND NEWER APPLIANCES. L SHAPED LAUNDRY AREA OFF KITCHEN.THIS IS A VERY NICE HOME AT A GREAT PRICE. BEST HOUSE ON THE MARKET FOR THE MONEY."
        },
        {
            "id": 16,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISjzumfa2p6dyo0000000000.webp",
            "address": "4833 W 123rd Pl, Chicago, IL 60803",
            "longitude": "-87.740200",
            "latitude": "41.667550",
            "price": 229700,
            "room": 3,
            "bath": 1,
            "size": 1564,
            "categories": "sale",
            "summary": "Check out this spacious brick home with 3 bedrooms, 1 bathroom and 3-car garage! Enter this updated throughout beautiful Ranch and be greeted by a living room with natural and hardwood flooring."
        },
        {
            "id": 17,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzzti9zwi1r6h0000000000.webp",
            "address": "9313 S Clifton Park Ave, Evergreen Park, IL 60805",
            "longitude": "-87.710070",
            "latitude": "41.723720",
            "price": 199900,
            "room": 3,
            "bath": 2,
            "size": 1632,
            "categories": "sale",
            "summary": "Gorgeous Home on a Beautiful Block in Evergreen Park. All you can ask for in a Home: Space to Entertain All Year Round."
        },
        {
            "id": 18,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISn2o2r7qwkl671000000000.webp",
            "address": "9101 S Blackstone Ave, Chicago, IL 60619",
            "longitude": "-87.587780",
            "latitude": "41.729420",
            "price": 47000,
            "room": 3,
            "bath": 1,
            "size": 1000,
            "categories": "sale",
            "summary": " Nice, cozy home in a great neighborhood. Needs a little TLC but is move in ready."
        },
        {
            "id": 19,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzvmypv8jdw790000000000.webp",
            "address": "1546 S Homan Ave, Chicago, IL 60623",
            "longitude": "-87.710609",
            "latitude": "41.859482",
            "price": 113000,
            "room": 3,
            "bath": 2,
            "size": 1532,
            "categories": "sale",
            "summary": "Great home for investor or buyer looking to make put their own design touches. This 3 bedroom 1 bathroom home is ready for you!"
        },
        {
            "id": 20,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISfgdhrxk73tcw1000000000.webp",
            "address": "12735 S Peoria St, Chicago, IL 60643",
            "longitude": "-87.643350",
            "latitude": "41.662100",
            "price": 114900,
            "room": 3,
            "bath": 1,
            "size": 1100,
            "categories": "sale",
            "summary": "Beautiful light filled remodeled home with everything you have been looking for! "
        },
        {
            "id": 21,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS7yltl58i2al11000000000.webp",
            "address": "7706 Beloit Ave, Bridgeview, IL 60455",
            "longitude": "-87.807660",
            "latitude": "41.751180",
            "price": 209900,
            "room": 3,
            "bath": 3,
            "size": 1151,
            "categories": "sale",
            "summary": "Attractive updated brick ranch with full basement! Freshly painted throughout with all new "
                       "stainless steel appliances. "
        },
        {
            "id": 22,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3zfy0uwjne2b1000000000.webp",
            "address": "5415 S Neva Ave, Chicago, IL 60638",
            "longitude": "-87.799810",
            "latitude": "41.793510",
            "price": 324900,
            "room": 5,
            "bath": 2,
            "size": 1200,
            "categories": "sale",
            "summary": "House Beautiful from the top to bottom! If you have been on the fence about moving, this one will make you start packing."
        },
        {
            "id": 23,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISvoyj7wqpm47u1000000000.webp",
            "address": "5344 S Ashland Ave, Countryside, IL 60525",
            "longitude": "-87.871710",
            "latitude": "41.792460",
            "price": 320000,
            "room": 4,
            "bath": 2,
            "size": 1377,
            "categories": "sale",
            "summary": "TOUR THIS HOME AND MAKE IT YOUR OWN. YOU WILL NOT BE DISAPPOINTED."
        },
        {
            "id": 24,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3jja8lw6cs7d0000000000.webp",
            "address": "1436 Scott Ave, Winnetka, IL 60093",
            "longitude": "-87.757570",
            "latitude": "42.118900",
            "price": 11240000,
            "room": 5,
            "bath": 3,
            "size": 2478,
            "categories": "sale",
            "summary": "Classic English Tudor, gracious floor plan and fine architectural details. Meticulously maintained"
        },
        {
            "id": 25,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzngsyemsp5ha1000000000.webp",
            "address": "18358 Dundee Ave, Homewood, IL 60430",
            "longitude": "-87.676400",
            "latitude": "41.555410",
            "price": 209700,
            "room": 4,
            "bath": 2,
            "size": 1194,
            "categories": "sale",
            "summary": " Homewood-Flossmoor HS School District! This charming 4 bedroom, 2 bathroom home welcomes you with refinished hardwood flooring and many updates throughout. "
        },
        {
            "id": 26,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3rdnooq1rke61000000000.webp",
            "address": "124 W 67th St, Westmont, IL 60559",
            "longitude": "-87.978000",
            "latitude": "41.766550",
            "price": 212000,
            "room": 2,
            "bath": 3,
            "size": 1400,
            "categories": "sale",
            "summary": "Superb Orchard Gate townhome located in beautiful Westmont! Welcome and enjoy this fantastic 2 bed, 2.1 bath townhome with desirable features! "
        },
        {
            "id": 27,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISf44mzvaby6g61000000000.webp",
            "address": "6901 S Oglesby Ave APT 11D, Chicago, IL 60649",
            "longitude": "-87.567810",
            "latitude": "41.769710",
            "price": 60000,
            "room": 3,
            "bath": 3,
            "size": 2000,
            "categories": "sale",
            "summary": "Wintage home ready to move in."
        },
        {
            "id": 28,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzrn4c0m7mns80000000000.webp",
            "address": "122879 Sun River Dr, Frankfort, IL 60423",
            "longitude": "-87.898740",
            "latitude": "41.474030",
            "price": 689000,
            "room": 5,
            "bath": 5,
            "size": 5300,
            "categories": "sale",
            "summary": "A Superb Executive Home. 1,000+ Sqft Master Suite With All Amenities."
        },
        {
            "id": 29,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISnu1kns9js4am0000000000.webp",
            "address": "3427 S Lombard Ave, Cicero, IL 60804",
            "longitude": "-87.777580",
            "latitude": "41.829430",
            "price": 299000,
            "room": 8,
            "bath": 3,
            "size": 3000,
            "categories": "sale",
            "summary": "INCREDIBLE OPPORTUNITY TO OWN THIS EXPANDED BUNGALOW.MUST SEE TO APPRICIATE."
        },
        {
            "id": 30,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzzh9m18puqk91000000000.webp",
            "address": "2052 Rownham Hill Rd, New Lenox, IL 60451",
            "longitude": "-87.946930",
            "latitude": "41.480940",
            "price": 399999,
            "room": 4,
            "bath": 3,
            "size": 2783,
            "categories": "sale",
            "summary": "Gorgeous and better than new in Bristol Park. Ready for you to move in and start the new year!"
        },
        {
            "id": 31,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISqhuc4tojnxjh1000000000.webp",
            "address": "556 N Central Ave, Chicago, IL 60644",
            "longitude": "-87.765480",
            "latitude": "41.890850",
            "price": 160000,
            "room": 5,
            "bath": 2,
            "size": 2667,
            "categories": "sale",
            "summary": "Yes, finally, it is the Pink and White House. Beautiful Victorian 2 story single family Colonial, 5 bdrm residence on oversize corner lot. "
        },
        {
            "id": 32,
            "image": "https://www.zillow.com/homedetails/1938-W-Waveland-Ave-Chicago-IL-60613/2081886006_zpid/",
            "address": "1938 W Waveland Ave, Chicago, IL 60613",
            "longitude": "-87.677800",
            "latitude": "41.948930",
            "price": 1650000,
            "room": 5,
            "bath": 5,
            "size": 4500,
            "categories": "sale",
            "summary": "MOVE IN JUST FOR THE HOLIDAYS!LOVE WHERE YOU LIVE! GREAT LOCATION.."
        },
        {
            "id": 33,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISniswdyzerm2g1000000000.webp",
            "address": "1450 N Fairfield Ave APT GR, Chicago, IL 60622",
            "longitude": "-87.695830",
            "latitude": "41.908010",
            "price": 149900,
            "room": 2,
            "bath": 1,
            "size": 335,
            "categories": "sale",
            "summary": "Condo Conversion Garden Unit in Stunning Greystone Building- One block from beautiful Humboldt Park!"
        },
        {
            "id": 34,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISblqnns7jb3xk0000000000.webp",
            "address": "5341 N Ravenswood Ave, Chicago, IL",
            "longitude": "-87.674050",
            "latitude": "41.979110",
            "price": 429900,
            "room": 4,
            "bath": 2,
            "size": 940,
            "categories": "sale",
            "summary": "This very cute bungalow offers four bedrooms, two baths and is much more spacious then it looks from the outside. "
        },
        {
            "id": 35,
            "image": "https://photos.zillowstatic.com/p_h/IS76gustqyg5bi1000000000.jpg",
            "address": "9331 W 135th St, Orland Park, IL 60462",
            "longitude": "-87.849100",
            "latitude": "41.644750",
            "price": 249000,
            "room": 4,
            "bath": 2,
            "size": 2550,
            "categories": "sale",
            "summary": "Great place to stay!"
        },
        {
            "id": 36,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISnaivvcqlwlex0000000000.webp",
            "address": "1100 W 87th St, Willow Springs, IL 60480",
            "longitude": "-87.864730",
            "latitude": "41.732340",
            "price": 324900,
            "room": 5,
            "bath": 4,
            "size": 2550,
            "categories": "sale",
            "summary": "Beautiful Contemporary Home in an upscale section of Willow Springs."
        },
        {
            "id": 37,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISv04wxge9m0m81000000000.webp",
            "address": "283 E 164th St, Harvey, IL 60426",
            "longitude": "-87.639980",
            "latitude": "41.591790",
            "price": 84900,
            "room": 4,
            "bath": 2,
            "size": 1200,
            "categories": "sale",
            "summary": "This is a lot of house for the money!! Great potential just waiting for you."
        },
        {
            "id": 38,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3fsy59l89afc1000000000.webp",
            "address": "3032 188th St, Lansing, IL 60438",
            "longitude": "-87.682010",
            "latitude": "41.472450",
            "price": 129954,
            "room": 2,
            "bath": 1,
            "size": 974,
            "categories": "sale",
            "summary": "Well cared for home ready to move in! Much larger than it looks. "
        },
        {
            "id": 39,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISrpgv7swpekyq1000000000.webp",
            "address": "474 Lakewood Blvd, Park Forest, IL 60466",
            "longitude": "-87.691770",
            "latitude": "41.485030",
            "price": 118000,
            "room": 3,
            "bath": 2,
            "size": 1539,
            "categories": "sale",
            "summary": "Pull up on brick paver driveway and enter open concept lay-out w/ double picture windows and lots of natural light. "
        },
        {
            "id": 40,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3fsy59l89afc1000000000.webp",
            "address": "3032 188th St, Lansing, IL 60438",
            "longitude": "-87.542831",
            "latitude": "41.553570",
            "price": 129954,
            "room": 3,
            "bath": 1,
            "size": 1046,
            "categories": "sale",
            "summary": "Don't miss this special opportunity to buy home"
        },
        {
            "id": 41,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISrpo5pm2uv8vs0000000000.webp",
            "address": "1340 W Chase Ave, Chicago, IL 60626",
            "longitude": "-87.665710",
            "latitude": "42.014110",
            "price": 550000,
            "room": 4,
            "bath": 2,
            "size": 2175,
            "categories": "sale",
            "summary": "This is the first time this home has been on the market in 20 years! You will fall in love the moment you step up the herringbone pattern, newly paved walkway that leads to the covered front porch."
        },
        {
            "id": 42,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISrldmvkon7crg1000000000.webp",
            "address": "7622 N Rogers Ave, Chicago, IL 60626",
            "longitude": "-87.667210",
            "latitude": "42.019990",
            "price": 572500,
            "room": 8,
            "bath": 3,
            "size": 4000,
            "categories": "sale",
            "summary": " Lots of light and open space in this unique 8 bedroom/3 bath"
        },
        {
            "id": 43,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzbfzp71kr7sr0000000000.webp",
            "address": "1815 W Chase Ave, Chicago, IL 60626",
            "longitude": "-87.676170",
            "latitude": "42.013310",
            "price": 350000,
            "room": 7,
            "bath": 2,
            "size": 1578,
            "categories": "sale",
            "summary": "A classic 2 story victorian in highly sought after rogers park. Featuring 5 true bedrooms and 2 full baths."
        },
        {
            "id": 44,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISrtv1uq26lqij0000000000.webp",
            "address": "1773 W Arthur Ave, Chicago, IL 60626",
            "longitude": "-87.674620",
            "latitude": "42.000120",
            "price": 309900,
            "room": 4,
            "bath": 3,
            "size": 2235,
            "categories": "sale",
            "summary": "Excellent opportunity! Spacious sun filled property that was used as 2 units but it is a single family home. You can use the existing floor plan or think of it as a blank canvas and create your own dream!"
        },
        {
            "id": 45,
            "image": "https://photos.zillowstatic.com/cc_ft_384/ISjnx4iu7m1hid1000000000.webp",
            "address": "3830 N Racine Ave, Chicago, IL 60613",
            "longitude": "-87.659410",
            "latitude": "41.952040",
            "price": 1299900,
            "room": 4,
            "bath": 5,
            "size": 4000,
            "categories": "sale",
            "summary": "Wide lot in Blaine School, spectacular 4 bedroom single family with 4.1 baths located on quiet cul de sac Racine. "
        },
        {
            "id": 46,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISnupyixtkhwm91000000000.webp",
            "address": "911 W Addison St, Chicago, IL 60613",
            "longitude": "-87.652350",
            "latitude": "41.947190",
            "price": 719000,
            "room": 5,
            "bath": 4,
            "size": 2502,
            "categories": "sale",
            "summary": "Tremendous opportunity! Spacious, light-filled Greystone ideally located in Lakeview near the lake, Wrigley, the Red Line, shopping & dining offers a versatile floor plan with four bedrooms on the second level, a master suite with private bath on the third level, and a large walkout lower level with a rec room, third full bath, and fabulous laundry room. "
        },
        {
            "id": 47,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISvs1dfltafnzi0000000000.webp",
            "address": "3842 N Alta Vista Ter # 3842, Chicago, IL 60613",
            "longitude": "-87.656630",
            "latitude": "41.951800",
            "price": 770000,
            "room": 2,
            "bath": 3,
            "size": 2275,
            "categories": "sale",
            "summary": "Give yourself something sparkly for the holidays"
        },
        {
            "id": 48,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS6m8rlp2jn34i0000000000.webp",
            "address": "6249 N Ridgeway Ave, Chicago, IL 60659",
            "longitude": "-87.722310",
            "latitude": "41.995130",
            "price": 489900,
            "room": 4,
            "bath": 4,
            "size": 2400,
            "categories": "sale",
            "summary": "Beautiful, spacious, and bright! Welcome home to your unbelievable Jumbo Georgian home in sought-after Peterson Park."
        },
        {
            "id": 49,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS7218e6q0c20a1000000000.webp",
            "address": "6133 N Lawndale Ave, Chicago, IL 60659",
            "longitude": "-87.720950",
            "latitude": "41.992900",
            "price": 499900,
            "room": 7,
            "bath": 4,
            "size": 2389,
            "categories": "sale",
            "summary": "Jumbo side entrance colonial on large lot with attached 1 car garage in the heart of Peterson Park."
        },
        {
            "id": 50,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzfqekr6bydzp1000000000.webp",
            "address": "3052 W Hood Ave, Chicago, IL 60659",
            "longitude": "-87.706370",
            "latitude": "41.993180",
            "price": 349500,
            "room": 4,
            "bath": 3,
            "size": 1800,
            "categories": "sale",
            "summary": "Custom built home has lots of beautiful wood thru out and makes u feel like you are living in the country."
        },
        {
            "id": 51,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS7y1e0f6s9nqd0000000000.webp",
            "address": "5917 N Washtenaw Ave, Chicago, IL 60659",
            "longitude": "-87.696480",
            "latitude": "41.989040",
            "price": 331811,
            "room": 5,
            "bath": 1,
            "size": 1907,
            "categories": "sale",
            "summary": "Buy it as an investment or enjoy it as your own home."
        },
        {
            "id": 52,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISjbcodbnwudek0000000000.webp",
            "address": "4429 N Keystone Ave, Chicago, IL 60630",
            "longitude": "-87.694580",
            "latitude": "41.961690",
            "price": 260000,
            "room": 4,
            "bath": 3,
            "size": 1100,
            "categories": "sale",
            "summary": "Cozy, sun-filled single-family home with 3bed, 3 bathrooms, 2 car garage in Albany Park."
        },
        {
            "id": 53,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3fwxrw60x7x10000000000.webp",
            "address": "6228 N Drake Ave, Chicago, IL 60659",
            "longitude": "-87.718060",
            "latitude": "41.994530",
            "price": 205000,
            "room": 3,
            "bath": 2,
            "size": 1906,
            "categories": "sale",
            "summary": " 3 bedrooms, 1.1 baths property, built in 1949"
        },
        {
            "id": 54,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISjrcfzvjwc8m21000000000.webp",
            "address": "6320 N Maplewood Ave, Chicago, IL 60659",
            "longitude": "-87.693770",
            "latitude": "41.996390",
            "price": 339000,
            "room": 3,
            "bath": 2,
            "size": 960,
            "categories": "sale",
            "summary": "CHARMING 3 BEDROOM, 2 BATH CHICAGO BUNGALOW IN DESIRABLE WEST RIDGE."
        },
        {
            "id": 55,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISf481medk5udp0000000000.webp",
            "address": "6213 N Fairfield Ave, Chicago, IL 60659",
            "longitude": "-87.697870",
            "latitude": "41.994340",
            "price": 367500,
            "room": 3,
            "bath": 3,
            "size": 1851,
            "categories": "sale",
            "summary": "Chicago Classic Bungalow in the West Ridge neighborhood. "
        },
        {
            "id": 56,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISfkgqjdq9wrp70000000000.webp",
            "address": "4119 N Ridgeway Ave, Chicago, IL 60618",
            "longitude": "-87.721000",
            "latitude": "41.956020",
            "price": 375000,
            "room": 4,
            "bath": 3,
            "size": 2400,
            "categories": "sale",
            "summary": "Vintage 4 bed/2.1 bath bungalow with room addition. Brick/frame combo has some updates."
        },
        {
            "id": 57,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISbd415326zkpo0000000000.webp",
            "address": "3050 N Oakley Ave, Chicago, IL 60618",
            "longitude": "-87.685840",
            "latitude": "41.937340",
            "price": 620000,
            "room": 3,
            "bath": 4,
            "size": 1992,
            "categories": "sale",
            "summary": "This wonderful single family has all the updates, recessed lights, upstairs laundry, juliet balcony from master bedroom. Uncover this hidden gem in the Lakeview/Roscoe Village/Hamlin Park area! "
        },
        {
            "id": 58,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISrd3hygr8xcs11000000000.webp",
            "address": "3925 N Francisco Ave, Chicago, IL 60618",
            "longitude": "-87.700370",
            "latitude": "41.952930",
            "price": 335000,
            "room": 4,
            "bath": 2,
            "size": 1860,
            "categories": "sale",
            "summary": "Amazing opportunity for someone with vision."
        },
        {
            "id": 59,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISv0kk32z002540000000000.webp",
            "address": "3627 N Saint Louis Ave, Chicago, IL 60618",
            "longitude": "-87.714790",
            "latitude": "41.947360",
            "price": 325000,
            "room": 4,
            "bath": 2,
            "size": 1463,
            "categories": "sale",
            "summary": "Opportunity is knocking! Hurry, this one own't last!!"
        },
        {
            "id": 60,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISbxjis7vt2w6m1000000000.webp",
            "address": "2906 N Spaulding Ave, Chicago, IL 60618",
            "longitude": "-87.710240",
            "latitude": "41.934100",
            "price": 229900,
            "room": 5,
            "bath": 1,
            "size": 1427,
            "categories": "sale",
            "summary": "Single family Bungalow in a HOT location! Bring in all your own ideas. "
        },
        {
            "id": 61,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISfo7mhrro0atg0000000000.webp",
            "address": "2444 N Keeler Ave, Chicago, IL 60639",
            "longitude": "-87.731940",
            "latitude": "41.925720",
            "price": 160000,
            "room": 3,
            "bath": 2,
            "size": 1306,
            "categories": "sale",
            "summary": "This property is a fixer-upper, handyman special."
        },
        {
            "id": 62,
            "image": "https://photos.zillowstatic.com/p_h/ISb9lvkrurdkbl0000000000.jpg",
            "address": "2312 N Keeler Ave, Chicago, IL 60639",
            "longitude": "-87.731970",
            "latitude": "41.923050",
            "price": 174900,
            "room": 3,
            "bath": 3,
            "size": 1600,
            "categories": "sale",
            "summary": "Great opportunity to get into Hermosa Park. Easy access to expressway and rail service."
        },
        {
            "id": 63,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISfk8okmhqdfwt1000000000.webp",
            "address": "1642 N Parkside Ave, Chicago, IL 60639",
            "longitude": "-87.767020",
            "latitude": "41.910610",
            "price": 225000,
            "room": 4,
            "bath": 2,
            "size": 2000,
            "categories": "sale",
            "summary": "Here is your chance to own a lovely home."
        },
        {
            "id": 64,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISfw91d6hg2xas1000000000.webp",
            "address": "1657 N Menard Ave, Chicago, IL 60639",
            "longitude": "-87.769850",
            "latitude": "41.910940",
            "price": 249000,
            "room": 4,
            "bath": 2,
            "size": 1177,
            "categories": "sale",
            "summary": "Newly Renovated Solid Brick Bungalow home featuring 4 full sized bedrooms 2 bathrooms."
        },
        {
            "id": 65,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISr1mfgcqoxxqi1000000000.webp",
            "address": "1646 N Menard Ave, Chicago, IL 60639",
            "longitude": "-87.770620",
            "latitude": "41.910660",
            "price": 258500,
            "room": 5,
            "bath": 2,
            "size": 990,
            "categories": "sale",
            "summary": "Welcome to the Austin Area. Beautiful updated 5 Bedroom, 2 Bathroom Cozy Brick House. "
        },
        {
            "id": 66,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISz3ppmz7uk1uy0000000000.webp",
            "address": "2334 N Keystone Ave, Chicago, IL 60639",
            "longitude": "-87.728220",
            "latitude": "41.923660",
            "price": 99000,
            "room": 5,
            "bath": 4,
            "size": 1570,
            "categories": "sale",
            "summary": "An Exquisite Property in the Hermosa neighborhood, close to the Logan Square Area."
        },
        {
            "id": 67,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISbx3itble3a7p1000000000.webp",
            "address": "2723 N Major Ave, Chicago, IL 60639",
            "longitude": "-87.768210",
            "latitude": "41.930050",
            "price": 259900,
            "room": 4,
            "bath": 7,
            "size": 1784,
            "categories": "sale",
            "summary": "Good space in this 4 bedroom well maintained home on quiet street in Belmont Cragin!"
        },
        {
            "id": 68,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3v0s6ldq0tt31000000000.webp",
            "address": "2142 N Kostner Ave, Chicago, IL 60639",
            "longitude": "-87.736740",
            "latitude": "41.920050",
            "price": 234900,
            "room": 4,
            "bath": 1,
            "size": 1292,
            "categories": "sale",
            "summary": "Must see!!!! This home located in up and coming HOT area of Hermosa, has been tastefully remodeled and updated. "
        },
        {
            "id": 69,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISvcxq20lt4dtm1000000000.webp",
            "address": "5522 W Schubert Ave, Chicago, IL 60639",
            "longitude": "-87.764670",
            "latitude": "41.929640",
            "price": 200000,
            "room": 4,
            "bath": 2,
            "size": 880,
            "categories": "sale",
            "summary": "BRING YOUR OWN DECORATIVE IDEAS FOR A GREAT STARTER HOME . DESIRABLE LOCATION CLOSE TO ALL ACCOMMODATING SHOPPING DINING PARK SCHOOLS AND MUCH MORE."
        },
        {
            "id": 70,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS3r1mvbssca9p1000000000.webp",
            "address": "2034 N Kilpatrick Ave, Chicago, IL 60639",
            "longitude": "-87.743970",
            "latitude": "41.917930",
            "price": 479000,
            "room": 4,
            "bath": 4,
            "size": 2592,
            "categories": "sale",
            "summary": "Upscale brand new construction home! This 4 bed 4 bath home has been design with detail in mind."
        },
        {
            "id": 71,
            "image": "https://photos.zillowstatic.com/cc_ft_768/IS7ip9ong98vpd1000000000.webp",
            "address": "2148 N Moody Ave, Chicago, IL 60639",
            "longitude": "-87.779460",
            "latitude": "41.919220",
            "price": 319900,
            "room": 5,
            "bath": 3,
            "size": 1547,
            "categories": "sale",
            "summary": "Beautiful 5 bedroom, 3 bath Octagon Bungalow! Open concept main level features spacious and sunny living areas with exquisite finishes plus 2 large bedrooms with a tandem office. "
        },
        {
            "id": 72,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISjvvk3n4rasyk0000000000.webp",
            "address": "2245 N Lowell Ave, Chicago, IL 60639",
            "longitude": "-87.734840",
            "latitude": "41.922030",
            "price": 315000,
            "room": 4,
            "bath": 2,
            "size": 1665,
            "categories": "sale",
            "summary": "Many updates in this sweet tri level home 4+1 bedroom home. Gleaming hardwood floors, new windows, freshly painted, new light fixtures and blinds. "
        },
        {
            "id": 73,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzn4zbs6ldi6h1000000000.webp",
            "address": "2108 N Tripp Ave, Chicago, IL 60639",
            "longitude": "-87.732990",
            "latitude": "41.919180",
            "price": 379900,
            "room": 5,
            "bath": 3,
            "size": 2200,
            "categories": "sale",
            "summary": "Few houses from Walt Disney's childhood home!! Close to public transportation, expressways, restaurants, grocery stores, and shopping centers. "
        },
        {
            "id": 74,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISr98atmm0kw1k1000000000.webp",
            "address": "4334 W Dickens Ave, Chicago, IL 60639",
            "longitude": "-87.694580",
            "latitude": "41.880270",
            "price": 318000,
            "room": 5,
            "bath": 3,
            "size": 1788,
            "categories": "sale",
            "summary": "Beautifully Updated, Super Spacious 5 Bed / 2.5 Bath Brick Bungalow in Hot Hermosa! Gleaming Hardwood Floors and Lovely Crown Moulding throughout first level."
        },
        {
            "id": 75,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISnqubh7q99s231000000000.webp",
            "address": "2170 N Major Ave, Chicago, IL 60639",
            "longitude": "-87.768510",
            "latitude": "41.920010",
            "price": 270000,
            "room": 3,
            "bath": 1,
            "size": 1000,
            "categories": "sale",
            "summary": "Remodeled brick ranch in highly sought Belmont-Cragin! This one has everything you're looking for: refinished hardwood floors through-out."
        },
        {
            "id": 76,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISbxjelbajtjsf0000000000.webp",
            "address": "5122 W Wrightwood Ave, Chicago, IL 60639",
            "longitude": "-87.754790",
            "latitude": "41.927990",
            "price": 249000,
            "room": 4,
            "bath": 2,
            "size": 3125,
            "categories": "sale",
            "summary": "This 3125 square foot single family home has 5 bedrooms and 3.0 bathrooms. It is located at 5122 W Wrightwood Ave Chicago, Illinois."
        },
        {
            "id": 77,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISr1281k9392fp1000000000.webp",
            "address": "1623 N Kedvale Ave, Chicago, IL 60639",
            "longitude": "-87.729740",
            "latitude": "41.910470",
            "price": 219900,
            "room": 3,
            "bath": 3,
            "size": 3000,
            "categories": "sale",
            "summary": "Excellent opportunity in Hermosa area, nice property with three full bathrooms, three bedrooms, family room, office space plus extra rooms in basement, two car garage. Hardwood floors, fresh paint. With a lot of potential. Easy to show."
        },
        {
            "id": 78,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISr9wk9pfw27sg0000000000.webp",
            "address": "2206 N Tripp Ave, Chicago, IL 60639",
            "longitude": "-87.733030",
            "latitude": "41.920930",
            "price": 990,
            "room": 3,
            "bath": 1,
            "size": 1177,
            "categories": "sale",
            "summary": "Charming 3 bedroom cottage on 25x125 lot plus a 2 car garage. Well sized front living space. White kitchen w/granite counters & island with breakfast bar."
        },
        {
            "id": 79,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzfudaangd2tz0000000000.webp",
            "address": "3142 S Stewart Ave, Chicago, IL 60616",
            "longitude": "-87.636110",
            "latitude": "41.836910",
            "price": 549000,
            "room": 3,
            "bath": 4,
            "size": 3000,
            "categories": "sale",
            "summary": "Well maintained 3 story contemporary home, newly renovated bedrooms with brand new hardwood floors. Kitchen features granite countertop and extended cabinets."
        },
        {
            "id": 80,
            "image": "https://photos.zillowstatic.com/p_h/ISqpodrhu4ow1r1000000000.jpg",
            "address": "3434 S Normal Ave, Chicago, IL 60616",
            "longitude": "-87.639060",
            "latitude": "41.831530",
            "price": 489000,
            "room": 3,
            "bath": 4,
            "size": 2400,
            "categories": "sale",
            "summary": "Beautiful single family home in the heart of Bridgeport. Recently updated with 3 levels of living space."
        },
        {
            "id": 81,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISr9478hcbzv310000000000.webp",
            "address": "1936 S Prairie Ave # B20, Chicago, IL 60616",
            "longitude": "-87.621400",
            "latitude": "41.856080",
            "price": 400000,
            "room": 2,
            "bath": 2,
            "size": 1268,
            "categories": "sale",
            "summary": "One of a Kind 2bed 2bath Condo Located in Historic Prairie District that Lives Like a Single Family Home Complete with Fenced in FRONT YARD and Attached Garage! Absolutely Charming Unit with Newer Appliances, Fresh Paint, Granite Counters w/Breakfast Bar, 42'' Cabinets, Hardwood Throughout and In Unit Washer and Dryer."
        },
        {
            "id": 82,
            "image": "https://photos.zillowstatic.com/cc_ft_384/ISb99mlo1kulnu0000000000.webp",
            "address": "4545 S Hermitage Ave, Chicago, IL 60609",
            "longitude": "-87.668260",
            "latitude": "41.810780",
            "price": 59900,
            "room": 8,
            "bath": 4,
            "size": 3100,
            "categories": "sale",
            "summary": "Half a block from the park!!This 3100 square foot multi family home has 8 bedrooms and 4.0 bathrooms. It is located at 4545 S Hermitage Ave Chicago, Illinois."
        },
        {
            "id": 83,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISfkooz2i4snkw1000000000.webp",
            "address": "2718 W Monroe St, Chicago, IL 60612",
            "longitude": "-87.694580",
            "latitude": "41.880270",
            "price": 99000,
            "room": 4,
            "bath": 2,
            "size": 1177,
            "categories": "sale",
            "summary": "This is a 4 bedroom, 2.0 bathroom, multi family home. It is located at 2718 W Monroe St Chicago, Illinois."
        },
        {
            "id": 84,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISjze6ots0203n0000000000.webp",
            "address": "3632 S Leavitt St, Chicago, IL 60609",
            "longitude": "-87.680340",
            "latitude": "41.827760",
            "price": 370000,
            "room": 4,
            "bath": 2,
            "size": 1800,
            "categories": "sale",
            "summary": "ARCHITECTURALLY REDESIGNED 4 BEDROOM, 2 BATH CHICAGO STYLED BUNGALOW READY TO BE ENJOYED WITH NEW OWNERS."
        },
        {
            "id": 85,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISr90shb1farcc0000000000.webp",
            "address": "842 W 54th St, Chicago, IL 60609",
            "longitude": "-87.646910",
            "latitude": "41.796200",
            "price": 119900,
            "room": 4,
            "bath": 2,
            "size": 966,
            "categories": "sale",
            "summary": "AFFORDABLE & NICELY REHABBED SPLIT LEVEL SINGLE FAMILY HOME! THIS HOME OFFERS AN OPEN LAYOUT, YOU WALK INTO A NICE SIZE LIVING & DINING ROOM WITH NEW LAMINATED WOOD FLOORING, NEW KITCHEN CABINETS WITH VINYL FLOORING, UPPER LEVEL OFFERS 3 BEDROOMS AND FULL BATH, LOWER LEVEL WITH ADDITIONAL BEDROOM, FAMILY ROOM AND HALF A BATH,WALK OUT TO A SPACIOUS BACKYARD WITH NEW PRIVACY WOOD FENCE ALL AROUND! "
        },
        {
            "id": 86,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISizuamnb8004v0000000000.webp",
            "address": "515 W 40th Pl, Chicago, IL 60609",
            "longitude": "-87.639190",
            "latitude": "-87.639190",
            "price": 210000,
            "room": 4,
            "bath": 2,
            "size": 1800,
            "categories": "sale",
            "summary": "In and out of the express way. Quiet block. Free snow removal service."
        },
        {
            "id": 87,
            "image": "https://photos.zillowstatic.com/p_h/ISbpp9z09elvb61000000000.jpg",
            "address": "5141 S Morgan St, Chicago, IL 60609",
            "longitude": "-87.694580",
            "latitude": "41.880270",
            "price": 99000,
            "room": 3,
            "bath": 2,
            "size": 672,
            "categories": "sale",
            "summary": "Great Opportunity with great potential. Spacious home right across the street from a public elementary school. "
        },
        {
            "id": 88,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISf0da1zh4lh6j1000000000.webp",
            "address": "455 W 38th St, Chicago, IL 60609",
            "longitude": "-87.638300",
            "latitude": "41.825200",
            "price": 559900,
            "room": 5,
            "bath": 4,
            "size": 3600,
            "categories": "sale",
            "summary": "Stately Bridgeport location for this almost new all brick custom three story home and it is just steps from the Chicago White Sox Park, the CTA Redline and easy access to downtown."
        },
        {
            "id": 89,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISfo7ujmf4itjm1000000000.webp",
            "address": "4360 S Shields Ave, Chicago, IL 60609",
            "longitude": "-87.634827",
            "latitude": "41.814510",
            "price": 185000,
            "room": 6,
            "bath": 3,
            "size": 1554,
            "categories": "sale",
            "summary": "Comiskey/Bridgeport/Fuller Park area. Drive by and you'll see! As nice inside as outside. "
        },
        {
            "id": 90,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISfkooz2i4snkw1000000000.webp",
            "address": "2718 W Monroe St, Chicago, IL 60612",
            "longitude": "-87.694580",
            "latitude": "41.880270",
            "price": 99000,
            "room": 4,
            "bath": 2,
            "size": 1177,
            "categories": "sale",
            "summary": "This is a 4 bedroom, 2.0 bathroom, multi family home. It is located at 2718 W Monroe St Chicago, Illinois."
        },
        {
            "id": 91,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISvc9o458wmt6k1000000000.webp",
            "address": "6652 S Woodlawn Ave, Chicago, IL 60637",
            "longitude": "-87.596370",
            "latitude": "41.773680",
            "price": 479000,
            "room": 4,
            "bath": 4,
            "size": 3100,
            "categories": "sale",
            "summary": "Woodlawn gut rehab of a Greystone two unit building, turned into a spacious single family home featuring 4 bedrooms and 4 full bathrooms."
        },
        {
            "id": 92,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISj3i76kdt7be20000000000.webp",
            "address": "6825 S Champlain Ave, Chicago, IL 60637",
            "longitude": "-87.608900",
            "latitude": "41.770340",
            "price": 129000,
            "room": 8,
            "bath": 3,
            "size": 2731,
            "categories": "sale",
            "summary": "New furnaces new Appliances new hot water tank new floors and many more . Blocks away from Obama foundation and University of Chicago green and red lines . "
        },
        {
            "id": 93,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISr90k3zfo4b7v1000000000.webp",
            "address": "1224 E 57th St, Chicago, IL 60637",
            "longitude": "-87.595310",
            "latitude": "41.791610",
            "price": 995000,
            "room": 4,
            "bath": 3,
            "size": 2765,
            "categories": "sale",
            "summary": "Welcome to this unique campus cottage, built around the Columbian Worlds Fair. Bright and open, spacious rooms."
        },
        {
            "id": 94,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISb1nbgpmnsjyp0000000000.webp",
            "address": "6652 S Wabash Ave, Chicago, IL 60637",
            "longitude": "-87.624270",
            "latitude": "41.773310",
            "price": 79900,
            "room": 4,
            "bath": 2,
            "size": 2200,
            "categories": "sale",
            "summary": "This vintage beauty is zoned multiple, but has been configured for many years as a single family residence. The 2nd floor is duplexed up to the finished attic."
        },
        {
            "id": 95,
            "image": "https://photos.zillowstatic.com/uncropped_scaled_within_1344_1008/ISfkooz2i4snkw1000000000.webp",
            "address": "1141 E 65th St, Chicago, IL 60637",
            "longitude": "-87.596880",
            "latitude": "41.776540",
            "price": 159900,
            "room": 3,
            "bath": 2,
            "size": 1900,
            "categories": "sale",
            "summary": "Great location !!Great condo alternative. Bring your design ideas. 3 bedrooms, one and a half. bath"
        },
        {
            "id": 96,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISq16vdsftjait0000000000.webp",
            "address": "5026 S Greenwood Ave, Chicago, IL 60615",
            "longitude": "-87.599810",
            "latitude": "41.803090",
            "price": 4500000,
            "room": 7,
            "bath": 10,
            "size": 17769,
            "categories": "sale",
            "summary": "THE GOODMAN MANSION- ONE OF THE MOST SIGNIFICANT HOMES IN CHICAGO! In the heart of historic Kenwood, this 1892 Queen Anne home was designed by Treat & Foltz and built by the Goodman Family (who gifted the Goodman Theater)."
        },
        {
            "id": 97,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISbpl2r65ia7tt0000000000.webp",
            "address": "5727 S Michigan Ave # G, Chicago, IL 60637",
            "longitude": "-87.621780",
            "latitude": "41.790140",
            "price": 99000,
            "room": 2,
            "bath": 2,
            "size": 1300,
            "categories": "sale",
            "summary": "2 bedroom, 2 bath condo. Recently painted throughout. Easy maintenance. Laundry in-unit."
        },
        {
            "id": 98,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISnudlonvs3uwe0000000000.webp",
            "address": "828 E 47th Pl, Chicago, IL 60615",
            "longitude": "-87.605330",
            "latitude": "41.808840",
            "price": 475000,
            "room": 4,
            "bath": 4,
            "size": 2500,
            "categories": "sale",
            "summary": "Stunning down to the studs full gut rehab of a corner row house in the historic Kenwood neighborhood. Professionally remodeled with preservation of elements of the original charm while incorporating modern luxury amenities."
        },
        {
            "id": 99,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISrlx9nls9ybeq0000000000.webp",
            "address": "3844 S Hermitage Ave, Chicago, IL 60609",
            "longitude": "-87.669270",
            "latitude": "41.823660",
            "price": 495000,
            "room": 4,
            "bath": 4,
            "size": 2200,
            "categories": "sale",
            "summary": "Unique & contemporary custom designed single family house in the McKinley Park. 4 bed 3.5 bath + 2.5 garage with very efficient layout. Complete Gut out and turn-key rehab project"
        },
        {
            "id": 100,
            "image": "https://photos.zillowstatic.com/cc_ft_768/ISzzx9pwzoihgq0000000000.webp",
            "address": "3313 S Calumet Ave, Chicago, IL 60616",
            "longitude": "-87.618040",
            "latitude": "41.834120",
            "price": 585000,
            "room": 8,
            "bath": 5,
            "size": 3486,
            "categories": "sale",
            "summary": "This 3486 square foot single family home has 8 bedrooms and 5.0 bathrooms. It is located at 3313 S Calumet Ave Chicago, Illinois."
        },


        {
            "id": 101,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/IS7uq68u3lahf81000000000.webp",
            "address": "1428 Oxford Ave, Claremont, CA 91711",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 850000,
            "room": 6,
            "bath": 3,
            "size": 2674,
            "categories": "sale",
            "summary": "Beautifully renovated light and bright 6 bedroom 3 bathroom home. Features include gleaming new kitchen with new white cabinets, quartz countertops, and stainless steel appliances. Couple that with sparkling new bathrooms, recessed lighting, laminate wood floors, two car garage and large lot and this is the ideal place to call home."
        },
        {
            "id": 102,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/ISr1amln7zh79z0000000000.webp",
            "address": "3419 Campus Ave, Claremont, CA 91711",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 589500,
            "room": 3,
            "bath": 2,
            "size": 1177,
            "categories": "sale",
            "summary": "The updated kitchen with granite counters and stainless-steel appliances offers room for a kitchen table, or additional counter space and storage."
        },
        {
            "id": 103,
            "image": "https://photos.zillowstatic.com/fp/b519e881de2c699c1166a62686fa1d6f-cc_ft_1536.webp",
            "address": "1268 Hillsdale Dr, Claremont, CA 91711",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 665000,
            "room": 4,
            "bath": 2,
            "size": 2010,
            "categories": "sale",
            "summary": "Well maintained Single family home located in the heart of Claremont. This Beautiful 1 Story Home features 4 BEDROOMS and 2 BATHS. 2,010 Living SF. and 11,725 sf. Lot Size"
        },
        {
            "id": 104,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/ISbdw6gxabi1o61000000000.webp",
            "address": "118 Bloom Dr, Claremont, CA 91711",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 464000,
            "room": 3,
            "bath": 3,
            "size": 1552,
            "categories": "sale",
            "summary": "Investor and homebuyer opportunity! This property is being offered at a live auction on 01-02-2020. Buy it as an investment or enjoy it as your own home."
        },
        {
            "id": 105,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/IS7azz04x1ojsn1000000000.webp",
            "address": "214 E College Way, Claremont, CA 91711",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 684900,
            "room": 3,
            "bath": 2,
            "size": 1942,
            "categories": "sale",
            "summary": "If you are looking for that perfect Mid-Century home, this is the one you have been waiting for. Don't miss this opportunity to own a home located in the Piedmont Mesa area! This home has an original mural from the prestigious Henderson builder. "
        },
        {
            "id": 106,
            "image": "https://photos.zillowstatic.com/fp/c9d6a3aebdb81f21577805327b5fc251-cc_ft_1536.webp",
            "address": "2531 N Mountain Ave, Claremont, CA 91711",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 1080000,
            "room": 3,
            "bath": 3,
            "size": 2377,
            "categories": "sale",
            "summary": "This custom built mid century modern home, located in the prestigious hillside community of Claraboya, truly has everything for today's discerning buyer. "
        },
        {
            "id": 107,
            "image": "https://photos.zillowstatic.com/cc_ft_1536/ISjz2ddoe3cqbw0000000000.webp",
            "address": "2384 2nd St, La Verne, CA 91750",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 619000,
            "room": 3,
            "bath": 2,
            "size": 1324,
            "categories": "sale",
            "summary": "Located in the sought-after neighborhood of Old Town La Verne, this beautiful 1901 Craftsman home on a corner lot has been lovingly maintained and is now available."
        },
        {
            "id": 108,
            "image": "https://photos.zillowstatic.com/fp/f62d6d27c29e98b219460b855b53d086-cc_ft_1536.webp",
            "address": "809 Arbor Cir, La Verne, CA 91750",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 550000,
            "room": 3,
            "bath": 2,
            "size": 1364,
            "categories": "sale",
            "summary": "Your holiday home awaits! Welcome to this pristine 3-bedroom, 2-bath turnkey home located in the exclusive gated community of Park La Verne!"
        },
        {
            "id": 109,
            "image": "https://photos.zillowstatic.com/fp/db018c138c2ffea19bf42876905616b8-uncropped_scaled_within_1536_1152.webp",
            "address": "714 W Carter Dr, Glendora, CA 91740",
            "longitude": "0.0",
            "latitude": "0.0",
            "price": 545000,
            "room": 4,
            "bath": 2,
            "size": 1572,
            "categories": "sale",
            "summary": "HUGE PRICE REDUCTION! TAKE A LOOK BEFORE IT'S TOO LATE! Beautiful pool home located in a quiet, family oriented neighborhood! This single story home has original wood flooring and has new paint throughout."
        }

    ]

    # return JsonResponse(houseData, safe=False)
    return houseData


if __name__ == '__main__':
    dsa = house_data()
    for di in dsa:
        print('claremont' in di['address'].lower())


    # insertData('')

    print('\n\nend')
