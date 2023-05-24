from django.shortcuts import redirect


def auth_customer(func):
    def wrapper(request):
        if "customer_sessionId" in request.session:
            return func(request)
        else:
            return redirect("customer:login")

    return wrapper
