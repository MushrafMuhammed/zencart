
from django.shortcuts import redirect, render

from seller.models import Product, Seller

# Create your views here.

def loginfun(request):
    msg = ''
    if request.method == 'POST' :
        base_username = request.POST['email']
        base_password = request.POST['password']

        try :
            seller = Seller.objects.get(
                 email = base_username,
                 password = base_password
            )
            request.session['seller_sessionID'] = seller.id
            return redirect('seller:addProducts')
        except :
            msg = 'invalid username or password !'

    return render(request, 'seller/login.html', {'errorMessage' : msg })

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


