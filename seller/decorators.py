from django.shortcuts import redirect


def auth_seller(func):
    def wrapper(request):
        if "seller_sessionId" in request.session:
            return func(request)
        else:
            return redirect("seller:login")

    return wrapper
