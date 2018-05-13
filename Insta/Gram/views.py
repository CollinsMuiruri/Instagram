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
