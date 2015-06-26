from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
import django.contrib.auth as auth_views

urlpatterns = [
    url(r'^(?P<pk>\d+)', DetailView.as_view(model=User), name='view_user'),
    url(r'^register/$', CreateView.as_view(model=User,
                            form_class=UserCreationForm,
                            success_url = "http://www.google.com"),
                            name='register'),
    url(r'^login/', auth_views.login, name='login'),

    # url(r'^', include('django.contrib.auth.urls')),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='view_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='view_logout'),
    # url(r'^login/$', auth_views.login), #, {'template_name': 'myapp/login.html'}),

]
