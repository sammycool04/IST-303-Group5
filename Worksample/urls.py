from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import house.views
from house.views import BootstrapFilterView

urlpatterns = [
    # path('', house.views.house, name = 'house'),
    # path('home.html', views.homepage, name = 'home'),
    path('', BootstrapFilterView, name = 'bootstrap'),
    path('admin/', admin.site.urls),
    path('signup.html', views.signup, name='signup')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
