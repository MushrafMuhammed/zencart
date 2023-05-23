from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginfun, name='login'),
    path('add-products', views.addproductsfun, name='addProducts'),
]
