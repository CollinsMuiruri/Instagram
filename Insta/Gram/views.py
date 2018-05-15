from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Image
from .forms import InfoImageForm,NewsLetterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def latest_images(request):
    date = dt.date.today()
    image = Image.todays_news()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name, email = email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('latest')

    else:
        form = NewsLetterForm()
    return render(request, 'allofinsta/insta-home.html', {"date": date,"image":image,"letterform":form})

@login_required(login_url='/accounts/login')
def search_results(request):
    searched_ = Image.search_by_title(search_term)

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        message = f"{search_term}"

        return render(request, 'allofinsta/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'allofinsta/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def image_detail(request,id):
    # return HttpResponse(slug)
    image = Image.objects.filter(id = id).all()
    return render(request,'allofinsta/home.html',{'image':image})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"allofinsta/image.html", {"image":image})

@login_required(login_url='/accounts/login')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = InfoImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
    else:
        form = InfoImageForm()
    return render(request, "new_image.html", {"form": form})
