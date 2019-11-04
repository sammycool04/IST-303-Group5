from django.contrib import admin

# Register your models here.
from .models import House, Host, Category

admin.site.register(House)
admin.site.register(Host)
admin.site.register(Category)
