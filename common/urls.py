from . import views
from django.urls import path

appname = 'common'

urlpatterns = [
    path('home', views.homefun, name='home' ),


]