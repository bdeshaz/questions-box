from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views
# import django.contrib.auth.views as auth_views

urlpatterns = [
    url(r'^u/(?P<pk>\d+)', DetailView.as_view(model=User,
                            template_name='users/user_detail.html',
                            ), name='view_user'),
    # url(r'^register/$', CreateView.as_view(model=User,
    #                         form_class=UserCreationForm,
    #                         success_url = '/questions/'),
    #                         name='register'),
    # url(r'^login/', auth_views.login, name='login'),
    # url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^users/$', ListView.as_view(model=User,
                            template_name='users/user_list.html',
                            context_object_name='users',
                            paginate_by=30), name='view_users')

    # url(r'^', include('django.contrib.auth.urls')),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='view_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='view_logout'),
    # url(r'^login/$', auth_views.login), #, {'template_name': 'myapp/login.html'}),

]
