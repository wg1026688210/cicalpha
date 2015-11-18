#coding: utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'dbManager/index.html')
def login(request):
    return render(request,'dbManager/login.html')
def login1(request):
    if request.POST['name']=='admin' and request.POST['Password']=='000000':
        return HttpResponseRedirect(reverse('dbManager:index'))
    else:
        p=u'账号密码错误'.encode("utf-8")
        context={'p':p}
        return render(request, 'dbManager/login.html',context)