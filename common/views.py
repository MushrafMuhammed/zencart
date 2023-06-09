from django.shortcuts import render
from customer.models import Cart

from seller.models import Product

# Create your views here.

def homefun(request):  
    if 'customer_sessionId' in request.session:
        cartItem = Cart.objects.filter(
            customer=request.session['customer_sessionId']
        )
        cartCount = cartItem.count()
        productsList = Product.objects.all() 
        cart_msg = request.session.pop("cart_msg", None)
    else:
        productsList = Product.objects.all()
        cartCount = 0
        cart_msg = request.session.pop("cart_msg", None)
    return render(request, 'common/home.html', {'products':productsList, 'cartCount': cartCount, 'cart_msg': cart_msg})


