from . import views
from django.urls import path

app_name = 'common'

urlpatterns = [
    path('home', views.homefun, name='home' ),
    

]