"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from task import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.home, name='home'), #主页
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'), #编辑任务
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'), #删除任务
    url(r'^finish/(?P<id>\d+)/$', views.finish, name='finish'), #完成任务
    url(r'^unfinish/(?P<id>\d+)/$', views.unfinish, name='unfinish'), #取消完成任务
    url(r'^browser/$', TemplateView.as_view(template_name="browser.html")), #重定向到一个网页
]
