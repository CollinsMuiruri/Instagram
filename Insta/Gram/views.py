from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def latest_images(request):
    date = dt.date.today()
    news = Image.todays_news()

    return render(request, 'allofinsta/base.html', {"date": date,})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'allofinsta/search.html',{"message":message,"articles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'allofinsta/search.html',{"message":message})
