from urllib.request import Request

from django.shortcuts import render, redirect, reverse
import re
from django.http import HttpResponseRedirect, HttpResponse
from django.template import context
from .models import myuser
from .forms import RegisterationForm, loginForm, EditForm
from django.views import View
from django.views.generic import ListView
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    context = {}
    email = request.session['Email']
    #password = request.session['password']
    users = myuser.objects.all()
    for user in users:
        if user.Email == email:
            context['user'] = user
            return render(request, 'home.html', context)
    #return HttpResponse(userr)
    #if users:


def login(request):
    context = {}
    form = loginForm()
    if (request.method == 'GET'):
        context['form'] = form
        return render(request, 'login.html', context)
    else:
        Email = request.POST['Email']
        password = request.POST['password']
        # check cred in User
        #authuser = authenticate(email=Email, password=password)
        # check cred in myuser
        user = myuser.objects.filter(Email=Email, password=password)

        if user:
            request.session['Email'] = Email

            return redirect(reverse('home'))
        else:
            context['errormsg'] = 'Invalid credentials'
            return render(request, 'login.html', context)


'''def mylogout(request):
    request.session['username'] = None
    return redirect('/affairs/loginusertoadmin')
'''

def register(request):
    context = {}
    form = RegisterationForm()
    if (request.method == 'GET'):
        context['form'] = form
        return render(request, 'register.html', context)
    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        Email = request.POST['Email']
        password = request.POST['password']
        conf = request.POST['confirm_password']
        phoneNum = request.POST['phone_number']
        img = request.POST['profile_picture']
        pattern = re.compile("^01[0125][0-9]{8}$")
        checkNum = pattern.match(phoneNum)
        checkPass = password == conf
        if not checkNum:
            context['errormsg'] = "Invalid phone number"
        elif not checkPass:
            context['errormsg'] = "Passwords don't match"
        else:
            myuser.objects.create(first_name=fname, last_name=lname, Email=Email,
                                  password=password, confirm_password=conf,
                                  phone_number=phoneNum, profile_picture=img)

        # add user
        #User.objects.create_user(email=Email, password=password)
        return render(request, 'register.html', context)

def edit(request):
    context={}
    if request.method == "GET":
        email = request.session['Email']
        users = myuser.objects.all()
        for user in users:
            if user.Email == email:
                context['current_user'] = user
                return render(request, 'edit.html', context)
    else:
        current_user = request.session['Email']
        profile = myuser.objects.get(Email=current_user)
        return HttpResponse(profile)
        form = EditForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            user = form.save()
            profile.profile_picture = myuser.profile_picture
            profile.save()
            #return redirect('user_profile')
        return render(request, 'edit.html', {'current_user': current_user, 'form': form})