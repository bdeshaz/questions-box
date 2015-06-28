from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views
# import django.contrib.auth.views as auth_views
from users.views import UserDetailView
from .views import edit_user, UserListView

urlpatterns = [
    url(r'^u/(?P<pk>\d+)', UserDetailView.as_view(), name='view_user'),

    url(r'^users/$', UserListView.as_view(), name='view_users'),
    url(r'^edit/', edit_user, name="edit_user"),
]
