from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('login', views.loginfun, name='login'),
    path('add-products', views.addproductsfun, name='addProducts'),
    path('logout', views.logoutfun, name='logout'),

]
