from urllib.request import Request

from django.shortcuts import render, redirect, reverse
import re
from django.http import HttpResponseRedirect, HttpResponse
from django.template import context
from .models import myuser
from .forms import RegisterationForm, loginForm, EditForm
from django.views import View
from urllib.request import Request

from django.shortcuts import render, redirect, reverse
import re
from django.http import HttpResponseRedirect, HttpResponse
from django.template import context
from .models import myuser
from .forms import RegisterationForm, loginForm, EditForm
from django.views import View
from django.views.generic import ListView, View, UpdateView

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token


# Create your views here.

def home(request):
    if request.method == 'GET':
        context = {}
        email = request.session['Email']
        # password = request.session['password']
        users = myuser.objects.all()
        for user in users:
            if user.Email == email:
                context['user'] = user
                return render(request, 'home.html', context)
        # return HttpResponse(userr)
        # if users:


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
        # authuser = authenticate(email=Email, password=password)
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
        # User.objects.create_user(email=Email, password=password)
        return render(request, 'register.html', context)


def edit(request):
    context = {}
    email = request.session['Email']
    users = myuser.objects.all()
    for user in users:
        if user.Email == email:
            context['current_user'] = user
    if request.method == "GET":
        return render(request, 'edit.html', context)
    else:

        if request.POST:
            user_form = EditForm(request.POST)

        if user_form.is_valid():

            userr = myuser.objects.get(Email=email)
            user_form = EditForm(request.POST, instance=userr)
            user_form.save()
            return redirect('home')
        else:
            userr = myuser.objects.get(Email=email)
            user_form = EditForm(instance=userr)

            return render(request, 'edit.html', {'form': user_form})

def delete(request):
    email = request.session['Email']
    myuser.objects.filter(Email=email).delete()
    return redirect('/login')


