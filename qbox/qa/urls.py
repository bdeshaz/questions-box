__author__ = 'briandeshazer'

from django.conf.urls import include, url
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from qa import models, views

urlpatterns = [
    url(r'^questions/', ListView.as_view(
                    model=models.Question,
                    template_name="questions.html",
                    context_object_name='questions',
                    paginate_by=30,
                    ), name='view_questions'),
    url(r'^ask/', CreateView.as_view(
                    model=models.Question,
                    template_name="ask.html",
                    fields=("title", "text"),
                    ), name='ask_question'),
    url(r'^q/(?P<pk>\d+)', views.QuestionDetailView.as_view(), name="show_question"),
]
