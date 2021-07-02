from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auctions.models import Listing
from . forms import add_listing
from . forms import Bidform
from django.contrib.auth.decorators import login_required
import os
from .models import User
import random
#from .forms import handle_uploaded_file




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

####Listing

def index(request):
   list=Listing.objects.all()
   ran=['bg-primary mb-3','bg-secondary mb-3','bg-success mb-3','bg-danger mb-3','bg-warning mb-3','bg-info mb-3','bg-light mb-3','bg-dark mb-3']
   pick=random.choice(ran)
   return render(request, "auctions/index.html",{
     "pick":pick,
     "list":list

   })

@login_required(login_url='/login')
def create(request):
    if request.method =="POST":

        form = add_listing(request.POST,request.FILES)
        if form.is_valid():
            head=form.cleaned_data["head"]
            body=form.cleaned_data["body"]
            file=request.FILES['file']
            with open(f'auctions/static/pic/{head}.png', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            #handle_uploaded_file(request.FILES['file'])

            p=Listing(title=head,describe=body)
            p.save()
        else:
            return render(request,"auctions/createlist.html", {
            "form":form
            })
    return render(request,"auctions/createlist.html", {
    "form":add_listing()
    })

@login_required(login_url='/login')
def get_pk(request,obj_no):
  if request.method == "POST":
    form = Bidform(request.POST)
    if form.is_valid():
        bet=form.cleaned_data["bid"]
        b=Listing.objects.filter(pk=obj_no).update(bid=bet)
        #b.save()

  list=Listing.objects.get(pk=obj_no)

  return render(request, "auctions/item.html",{
       "list":list,
       "form":Bidform()
 })
