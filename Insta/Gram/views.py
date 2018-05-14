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

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name, email = email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('newsToday')

    else:
        form = NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterform":form})

def search_results(request):
    searched_ = Image.search_by_title(search_term)

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        message = f"{search_term}"

        return render(request, 'allofinsta/search.html',{"message":message,"articles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'allofinsta/search.html',{"message":message})
