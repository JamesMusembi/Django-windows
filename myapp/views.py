from django.shortcuts import render

# Create your views here.

def myview(request):
    return render(request, "index.html")

def home_screen_view(request):
    print(request.headers)
    return render(request, "base.html")