from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Sum
from django.http import JsonResponse
from customer.models import Cart
from customer.models import Customer

from seller.models import Product

# Create your views here.


def loginfun(request):
    msg = ""
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        try:
            customer = Customer.objects.get(email=username, password=password)
            request.session["customer_sessionId"] = customer.id
            return redirect("common:home")
        except:
            msg = "invalid password or username"

    return render(request, "customer/login.html", {"error_message": msg})


def viewCartfun(request):
    cartProducts = Cart.objects.filter(customer=request.session["customer_sessionId"])
    cartCount = cartProducts.count()

    
    subTotal = cartProducts.aggregate(total_price=Sum("price")).get(
        "total_price", 0
    )  # aggregation functions Sum(),


    if subTotal is None:
        subTotal = 00.00
    
    return render(request,"customer/cart.html",
        {"cartProducts": cartProducts, "cartCount": cartCount, "subTotal": subTotal})


def cartfun(request, pro_id):
    product = Product.objects.get(id=pro_id)
    if "customer_sessionId" in request.session:
        product_exist = Cart.objects.filter(
            product_details=pro_id, customer=request.session["customer_sessionId"]
        ).exists()

        if not product_exist:
            cart = Cart(
                customer_id=request.session["customer_sessionId"],
                product_details_id=pro_id,
                quantity=1,
                price=product.price,
            )
            cart.save()
            return viewCartfun(request)

        else:
            request.session["cart_msg"] = "item already in your cart"
            return redirect(reverse("common:home"))
    else:
        return redirect("customer:login")


def delCartfun(request, cart_id):
    delItem = Cart.objects.get(
        id=cart_id, customer=request.session["customer_sessionId"]
    )
    delItem.delete()
    return redirect("customer:viewCart")


def update_itemTotal(request):
    quantity = request.POST["quantity"]
    pro_id = request.POST["pro_id"]

    product = Product.objects.filter(id=pro_id).values("price")

    total = int(quantity) * product[0]["price"]
    print(total)

    # Update the Cart with the new price and quantity
    Cart.objects.filter(
        product_details_id=pro_id,
        customer_id=request.session["customer_sessionId"]
    ).update(quantity=quantity, price=total)

    return JsonResponse({"subTotal": total})
