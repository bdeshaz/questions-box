from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

urlpatterns = [
    url(r'(?P<pk>\d+)', DetailView.as_view(model=User), name='view_user')
    # url(r'^', include('django.contrib.auth.urls')),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='view_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='view_logout'),
    # url(r'^login/$', auth_views.login), #, {'template_name': 'myapp/login.html'}),

]
