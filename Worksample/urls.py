from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import house.views as vw


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.homepage, name='homepg'),
    path('home.html', views.homepage, name='homepg'),
    path('signup.html', views.signup, name='signup'),
    path('signin.html', views.signin, name='signin'),

    path('searchByAdd.html', views.searchByAdd, name='searchByAdd'),
    path('searchByPre.html', views.searchByPre, name='searchByPre'),
    path('survey.html', views.survey, name='survey'),
    path('map.html', views.showMap, name='showmap'),


    path('sbAdd', views.searchByAddResult, name='sbAdd'),
    path('sbPre', views.searchByPreResult, name='sbPre'),

    path('insertData', vw.insertData, name='insertD'),





    # ..............................................................

    path('zillow.html', views.zillow, name='zillow'),
    path('bootstrap_form.html', vw.BootstrapFilterView, name='Bootstrapform')


    # path('getForm', views.getForm, name='getForms')









] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
