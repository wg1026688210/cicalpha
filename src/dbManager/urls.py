"""cicalpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.flogin,name='login'),
    url(r'^login1/$',views.login1,name='login1'),
    url(r'^quit/$', views.quit),
    url(r'^menu/query/$',views.QueryView.as_view(),name='menu_query'),
    url(r'^menu/(?P<id>[0-9]+)/delete/$',views.delete,name='menu_delete'),
    url(r'^menu/insert/$',views.insert,name='menu_insert'),
    url(r'^menu/(?P<id>[0-9]+)/queryone/$',views.queryone,name='menu_queryone'),
    url(r'^menu/update/$',views.update,name='menu_update'), 
]
