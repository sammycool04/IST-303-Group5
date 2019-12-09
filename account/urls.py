from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import house.views as vw

urlpatterns = [
        path('signup', views.signup, name='signup'),
        path('signin', views.signin, name='signin'),
        path('signout', views.signout, name = 'signout'),
]
