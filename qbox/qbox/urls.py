"""qbox URL Configuration

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
from django.contrib import admin, auth
from django.views.generic import ListView
from qa.models import Question
from qa.views import MyRegistrationView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/profile', ListView.as_view(
        model=Question,
        template_name="qa/questions.html",
        context_object_name='questions',
        paginate_by=30,
    )),
    url(r'^', include('qa.urls')),
    url(r'^', include('users.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]  # url(r'^accounts/', include('django.contrib.auth.urls')),
