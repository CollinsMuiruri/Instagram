from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.db import transaction
from .models import Image,Profile
from .forms import InfoImageForm,NewsLetterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def latest_images(request):
    date = dt.date.today()
    image = Image.todays_images()

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
    image = Image.objects.filter(id = id)
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

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):

    current_user = request.user


    profiles = Image.objects.filter(editor__username__iexact=profile_id)
    # print(profiles)
    profile = Profile.objects.get(user__username__exact=profile_id)
    content = {
        "profiles":profiles,
        "profile":profile,
        "user": current_user,
        "profile_id": profile_id
    }
    return render(request,"profiles/profile.html", content)



# @login_required(login_url='/accounts/login/')
# def profile(request):
#     test = 'Profile route Working'
#     current_user = request.user
#     images = Image.objects.filter(creator=request.user)
#     profiles = Profile.objects.filter(user=request.user)
#     content = {
#         "test": test,
#         "current_user": current_user,
#         "images": images,
#         "profiles": profiles
#     }
#     return render(request, 'profiles/profile.html', content)
#
# @login_required(login_url='/accounts/login/')
# @transaction.atomic
# def add_profile(request):
#     test = 'Edit profile route working'
#     current_user = request.user
#     user_profile = Profile.objects.filter(user_id=current_user)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             user_profile = form.save(commit=False)
#             user_profile.user = current_user
#             user_profile.save()
#             return redirect('insta-home.html')
#     else:
#         form = ProfileForm(instance=request.user)
#
#         content = {
#             "test": test,
#             "form": form,
#         }
#         return render(request, 'profiles/edit-profile.html', content)
