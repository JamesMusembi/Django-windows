from django.shortcuts import render

# Create your views here.

def myview(request):
    return render(request, "index.html")

def home_screen_view(request):
    context = {}
    # context = {}
    # context['some_string'] = "this is some string that I'm passing to view"
    # context = (
    #     'some_string':"this is some string that I'm passing to view",

    # )
    list_of_values =[]
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    list_of_values.append("third entry")
    list_of_values.append("fourth entry")
    context['list_of_values'] = list_of_values


    return render(request, "myapp/home.html", context)