from django.shortcuts import render

# Create your views here.
# "Collection of functions or classes that handles the 
# logic the app process when user visits dif urls

from django.shortcuts import render

def home(request):
    # render home.html
    return render(request, "pages/home.html", {})
