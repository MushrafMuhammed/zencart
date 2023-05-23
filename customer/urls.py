from . import views
from django.urls import path

app_name = 'customer'

urlpatterns = [
    path('login', views.loginfun, name='login' ),
    path('logout', views.logoutfun, name='logout'),
    path('cart', views.viewCartfun, name='viewCart' ),
    path('cart/<int:pro_id>', views.cartfun, name='cart' ),
    path('delCart/<int:cart_id>', views.delCart, name='delCart'),
    path('update_itemTotal', views.update_itemTotal, name='update_itemTotal'),
    path('checkout', views.checkout, name='checkout'),
    path('success_page', views.success_page, name='success_page')


    

    # path('delCart/<int:pro_id>', views.delCart, name='delCart' ),
]