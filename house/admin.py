from django.contrib import admin

# Register your models here.

# from .models import House
# admin.site.register(House)

from .models import House, HouseInfo

admin.site.register(House)
admin.site.register(HouseInfo)



# admin.site.register(Host)
# admin.site.register(Category)
