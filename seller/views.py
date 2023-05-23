
from django.shortcuts import redirect, render
from seller.decorators import auth_seller

from seller.models import Product, Seller

# Create your views here.

def loginfun(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            seller = Seller.objects.get(
                email=username,
                password=password
            )
            request.session["seller_sessionId"] = seller.id
            return redirect("seller:addProducts")
        except:
            msg = "invalid password or username"

    return render(request, "seller/login.html", {"error_message": msg})

def logoutfun(request):
    del request.session['seller_sessionId']
    return redirect('seller:login')


def addproductsfun(request):
    if request.method == "POST":
        base_name = request.POST['name']
        base_description = request.POST['description']
        base_price = request.POST['price']
        base_current_stock = request.POST['current_stock']
        base_image = request.FILES['image']

        newProduct = Product(
            name = base_name,
            description = base_description,
            current_stock = base_current_stock,
            price = base_price,
            image = base_image,
        )
        newProduct.save()
    
    return render(request, 'seller/add_products.html')


