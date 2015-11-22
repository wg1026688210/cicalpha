#coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from cicalpha import settings
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Menu
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
class QueryView(generic.ListView):
    template_name='dbManager/MenuCrud/query_menu.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        return Menu.objects.all()
def delete(request, id):
    try:
        p = get_object_or_404(Menu,pk=id)
    except (KeyError,Menu.DoesNotExist):
        return render(request, 'dbManager/MenuCrud/query_menu.html', {
            'error_message': "You didn't select a choice.",
        })
    else:
        p.delete()
    return HttpResponseRedirect(reverse('dbManager:menu_query'))
def insert(request):
    M=Menu(url=request.POST['url'],name=request.POST['name'],isenable=request.POST['isenable'],parentid=request.POST['parentid'],level=request.POST['level'])
    M.save()
    return HttpResponseRedirect(reverse('dbManager:menu_query'))
def queryone(request,id):
    menu = get_object_or_404(Menu, pk=id)
    context = {'menu': menu}
    return render(request, 'dbManager/MenuCrud/queryone_menu.html', context)
def update(request):
    menu_id=request.POST['id']
    m = get_object_or_404(Menu,pk=menu_id)
    if(request.POST['url']!=None):
        m.url=request.POST['url']
    if(request.POST['name']!=None):
        m.name=request.POST['name']
    if(request.POST['isenable']!=None):
        m.isenable=request.POST['isenable']
    if(request.POST['parentid']!=None):
        m.parentid=request.POST['parentid']
    if(request.POST['level']!=None):
        m.level=request.POST['level']       
        m.save()
        return HttpResponseRedirect(reverse('dbManager:menu_query'))
