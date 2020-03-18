from django.shortcuts import render
from appone.forms import userform, userprotfform
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'appone/baseAppone.html')

# home
def home(request):
    return render(request, 'home.html')


def in_form(request):
    registered = False
    if request.method == "POST":

        user_form = userform(data=request.POST)
        protform = userprotfform(data=request.POST)

        if user_form.is_valid() and protform.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            prouser = protform.save(commit=False)
            prouser.user = user
            if 'profilepic' in request.FILES:
                prouser.profilepic = request.FILES['profilepic']
            prouser.save()
            registered = True
        else:
            print("not valid")
    else:
        user_form = userform()
        protform = userprotfform()
    return render(request, 'appone/register.html',
                  context={'registred': registered, 'user_form': user_form, 'user_prot': protform})

def user_login(request):
    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        user= authenticate(password=password,username=username)
        if user:
            a=1
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("not active")
        else:
            return HttpResponse("not authenticate")
    return render(request,'appone/login.html',{})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
