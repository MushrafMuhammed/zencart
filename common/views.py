from django.shortcuts import render

# Create your views here.

def homefun(request):
    return render(request, 'common/home.html')



