from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import house.views
from house.views import BootstrapFilterView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', house.views.house, name = 'house'),
    # path('home.html', views.homepage, name = 'home'),
    # path('', BootstrapFilterView, name = 'bootstrap'),


    path('', views.homepage, name='homepg'),
    path('home.html', views.homepage, name='homepg'),
    path('signup.html', views.signup, name='signup'),

    path('searchByAdd.html', views.searchByAdd, name='searchByAdd'),
    path('searchByPre.html', views.searchByPre, name='searchByPre'),

    path('sbAdd', views.searchByAddResult, name='sbAdd'),
    path('sbPre', views.searchByPreResult, name='sbPre'),


    path('bootstrap_form.html', BootstrapFilterView, name='Bootstrapform')



    # path('getForm', views.getForm, name='getForms')









] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
