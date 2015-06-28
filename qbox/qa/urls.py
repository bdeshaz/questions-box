from django.conf.urls import include, url
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from qa import models, views

urlpatterns = [
    url(r'^questions/', ListView.as_view(
                    model=models.Question,
                    template_name="qa/questions.html",
                    context_object_name='questions',
                    paginate_by=30,
                    ), name='view_questions'),

    url(r'^tags/', ListView.as_view(
                    model=models.Tag,
                    template_name="tags/tags.html",
                    context_object_name='tags',
                    paginate_by=30,
                    ), name='view_tags'),

    url(r'^ask/', views.AskQuestionView.as_view(), name='ask_question'),
    url(r'^q/(?P<pk>\d+)', views.QuestionDetailView.as_view(), name="show_question"),
    url(r'^q_tag/(?P<pk>\d+)', views.AddTagView.as_view(), name="add_tag"),
    url(r'^tag/(?P<pk>\d+)', views.TagDetailView.as_view(), name="view_tag"),
    url(r'^dtag/(?P<pk>\d+)', DeleteView.as_view(
                    model=models.Tag,
                    success_url='/tags/',), name="delete_tag"),

    # Voting redirect views
    url(r'^Qdownvote/(?P<pk>\d+)', views.QuestionDownvoteView.as_view(),
                                        name='question_downvote'),
    url(r'^QCupvote/(?P<pk>\d+)', views.QuestionCommentUpvoteView.as_view(),
                                        name='question_comment_upvote'),
    #   on answers
    url(r'^Aupvote/(?P<pk>\d+)', views.AnswerUpvoteView.as_view(),
                                        name='answer_upvote'),
    url(r'^Adownvote/(?P<pk>\d+)', views.AnswerDownvoteView.as_view(),
                                        name='answer_downvote'),
    url(r'^Qupvote/(?P<pk>\d+)', views.QuestionUpvoteView.as_view(),
                                        name='question_upvote'),
    url(r'^ACupvote/(?P<pk>\d+)', views.AnswerCommentUpvoteView.as_view(),
                                        name='answer_comment_upvote'),

]
