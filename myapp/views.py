from django.shortcuts import render

# Create your views here.

def myview(request):
    return render(request, "index.html")

def home_screen_view(request):
    context = {}
    context['some_string'] = "this is some string that I'm passing to view"
    
    return render(request, "myapp/home.html")