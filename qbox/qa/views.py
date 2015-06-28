from django.shortcuts import render
import django.views.generic as django_views
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from qa.models import Question, Answer, Tag, AnswerComment, QuestionComment, \
    QuestionUpvote, AnswerUpvote, QuestionDownvote, AnswerDownvote, \
    AnswerCommentUpvote, QuestionCommentUpvote
import qa.forms as QA_forms

from django.views.generic import View, RedirectView, ListView
# Create your views here.
from registration.backends.simple.views import RegistrationView

# Begin question and answer vote redirects
class QuestionUpvoteView(django_views.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'show_question'

    def dispatch(self, *args, **kwargs):
        question = Question.objects.get(pk=kwargs['pk'])
        voter = self.request.user
        if voter is not None and voter.is_authenticated():
            vote = QuestionUpvote(parent=question, voter=voter)
            vote.save()
            message_text = "You have upvoted this question."
            messages.add_message(self.request, messages.SUCCESS, message_text)
        return super(QuestionUpvoteView, self).dispatch(*args, **kwargs)


class QuestionDownvoteView(django_views.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'show_question'

    def dispatch(self, *args, **kwargs):
        question = Question.objects.get(pk=kwargs['pk'])
        voter = self.request.user
        if voter is not None and voter.is_authenticated():
            vote = QuestionDownvote(parent=question, voter=voter)
            vote.save()
            message_text = "You have downvoted this question."
            messages.add_message(self.request, messages.SUCCESS, message_text)
        return super(QuestionDownvoteView, self).dispatch(*args, **kwargs)


class AnswerUpvoteView(django_views.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'show_question'

    def dispatch(self, *args, **kwargs):
        answer = Answer.objects.get(pk=self.kwargs['pk'])
        voter = self.request.user
        if voter is not None and voter.is_authenticated():
            vote = AnswerUpvote(parent=answer, voter=voter)
            vote.save()
            message_text = "You have upvoted that answer."
            messages.add_message(self.request, messages.SUCCESS, message_text)
        return super(AnswerUpvoteView, self).dispatch(*args, **kwargs)



class AnswerDownvoteView(django_views.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'show_question'

    def dispatch(self, *args, **kwargs):
        answer = Answer.objects.get(pk=self.kwargs['pk'])
        voter = self.request.user
        if voter is not None and voter.is_authenticated():
            vote = AnswerDownvote(parent=answer, voter=voter)
            vote.save()
            message_text = "You have downvoted that answer."
            messages.add_message(self.request, messages.SUCCESS, message_text)
        return super(AnswerDownvoteView, self).dispatch(*args, **kwargs)

# comment upvote redirects
class QuestionCommentUpvoteView(django_views.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'show_question'

    def dispatch(self, *args, **kwargs):
        comment = QuestionComment.objects.get(pk=kwargs['pk'])
        voter = self.request.user
        if voter is not None and voter.is_authenticated():
            vote = QuestionCommentUpvote(parent=comment, voter=voter)
            vote.save()
            message_text = "You have upvoted that comment."
            messages.add_message(self.request, messages.SUCCESS, message_text)
        return super(QuestionCommentUpvoteView, self).dispatch(*args, **kwargs)


class QuestionDetailView(django_views.ListView):  # used to be ListView
    template_name = 'qa/question.html'
    model = Answer
    context_object_name = 'answers'
    paginate_by = 30
    question = None

    def dispatch(self, *args, **kwargs):
        self.question = Question.objects.get(pk=self.kwargs['pk'])
        return super(QuestionDetailView, self).dispatch(*args, **kwargs)

    # def get(self, request):
    #     return render(request, 'question.html', {})

    def get_queryset(self):
        return self.question.answer_set.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        self.question.set_show(self.request.user)
        context['question'] = self.question
        context['answer_form'] = QA_forms.AnswerForm()
        # question_comment_forms = []
        # for answer in self.question.answer_set:
        #     question_comment_forms.append(QA_forms.QuestionCommentForm())
        # form = MyForm(initial={'ids': [o.id for o in queryset]})
        # context['answer_comment'] = QA_forms.AnswerCommentForm()
        context['question_comment'] = QA_forms.QuestionCommentForm()
        # context['tag_form'] = QA_forms.TagForm()
        return context

    def post(self, *args, **kwargs):
        user = self.request.user
        if user is not None and user.is_authenticated():
            if 'answer_form' in self.request.POST:
                answer_form = QA_forms.AnswerForm(self.request.POST)
                answer = answer_form.save(commit=False)
                answer.owner = user
                answer.parent = self.question
                answer.save()
                message_text = "Your answer has been added. Thanks for contributing."
                messages.add_message(self.request, messages.SUCCESS, message_text)
            elif 'question_comment' in self.request.POST:
                question_comment = QA_forms.QuestionCommentForm(self.request.POST)
                comment = question_comment.save(commit=False)
                comment.owner = user
                comment.parent = self.question
                comment.save()
                message_text = "Your comment has been added. Remember to be civil."
                messages.add_message(self.request, messages.SUCCESS, message_text)
            elif 'answer_comment' in self.request.POST:
                pass
        else:
            message_text = "Log in to post things."
            messages.add_message(self.request, messages.ERROR, message_text)
        return redirect("/q/"+str(self.question.id))


class AskQuestionView(django_views.edit.CreateView):  # or FormView
    model = Question
    template_name = "qa/ask.html"
    fields = ["title", "text"]
    success_url = 'ask_question'
    # success_url = 'http://www.google.com'

    def form_valid(self, form):
        user = self.request.user
        if user is not None and user.is_authenticated():
            question = form.save(commit=False)
            question.owner = user
            question.save()
            message_text = "Your question has been added."
            messages.add_message(self.request, messages.SUCCESS, message_text)
        else:
            message_text = "Log in to ask questions."
            messages.add_message(self.request, messages.ERROR, message_text)
        return super(AskQuestionView, self).form_valid(form)


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/questions/'
