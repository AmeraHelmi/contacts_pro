"""amera URL Configuration

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
from django.contrib import admin
from myapp.views import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^amera/$',start),
    url(r'^contact/$',contact),
    url(r'^addcontact/$',addcontact),
    url(r'^allcontacts/$',allcontacts),
    url(r'^del/(?P<uid>\d+)',del_contact),
    url(r'^update/(?P<uid>\d+)',update_contact),
    url(r'^upcontact/(?P<uid>\d+)',up_contact),
    url(r'^find/$',find),
    url(r'^findcontact/$',findcontact),
    # url(r'^ajaxexample_json/$',ajax),
    
]
