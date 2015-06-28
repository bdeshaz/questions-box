from django.conf.urls import include, url
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from qa import models, views

urlpatterns = [
    url(r'^questions/', ListView.as_view(
                    model=models.Question,
                    template_name="qa/questions.html",
                    context_object_name='questions',
                    paginate_by=30,
                    ), name='view_questions'),
    url(r'^ask/', views.AskQuestionView.as_view(), name='ask_question'),
    url(r'^q/(?P<pk>\d+)', views.QuestionDetailView.as_view(), name="show_question"),
    url(r'^Aupvote/(?P<pk>\d+)', views.AnswerUpvoteView.as_view(), name='answer_upvote'),
    url(r'^Adownvote/(?P<pk>\d+)', views.AnswerDownvoteView.as_view(), name='answer_downvote'),
    url(r'^Qupvote/(?P<pk>\d+)', views.QuestionUpvoteView.as_view(), name='question_upvote'),
    url(r'^Qdownvote/(?P<pk>\d+)', views.QuestionDownvoteView.as_view(), name='question_downvote'),
]
