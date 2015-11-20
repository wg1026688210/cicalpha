#coding: utf-8
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from cicalpha import settings
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'dbManager/index.html')
def flogin(request):
    return render(request,'dbManager/login.html')
@csrf_exempt
def login1(request):
    username=request.POST['name']
    password=request.POST['Password']
    user =authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('dbManager:index'))
        else:
            return HttpResponseRedirect(reverse('dbManager:login'))
    else:
        return HttpResponseRedirect(reverse('dbManager:login'))
def quit(request):
    logout(request)
    return HttpResponseRedirect(reverse('dbManager:login'))