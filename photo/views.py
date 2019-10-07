from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url,include
from .models import Location, tags, Category, Image
# Create your views here.


#HOME PAGE VIEW FUNCTION
#########################

def index(request):
    photos = Image.objects.all()
    context = {'photos': photos}
    return render( request, 'home.html', {'photos': photos})

#LOCATION Page View Function!
def location(request):

    return render(request,'location.html',)

#CATEGORY Page View Function!

def category(request):
    return render(request,'category.html',)

#SEARCH CAPABILITY Page View Function!

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categorys": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})


