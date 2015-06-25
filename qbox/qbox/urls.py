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
from django.contrib import admin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from qa import models, views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^qa/', include('qa.urls')),
    url(r'^questions/', ListView.as_view(
                    model=models.Question,
                    template_name="questions.html",
                    context_object_name='questions',
                    paginate_by=30,
                    ), name='questions'),
    url(r'^ask/', CreateView.as_view(
                    model=models.Question,
                    template_name="ask.html",
                    ), name='ask_question'),
    url(r'^q/(?P<pk>\d+)', QuestionDetailView.as_view(), name="show_question")
]
