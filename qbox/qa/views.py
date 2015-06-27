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


class AnswerUpvote(django_views.RedirectView):
    permanent = True
    answer = None
    voter = None

    def dispatch(self, *args, **kwargs):
        self.answer = Answer.objects.get(pk=self.kwargs['pk'])
        self.voter = request.user
        vote = AnswerUpvote(parent=self.answer, voter=self.voter)
        vote.save()
        return super(AnswerUpvote, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        # return render(self.request, "question.html")
        return redirect('show_question', self.answer.parent.id)


class QuestionDetailView(django_views.View):  # used to be ListView
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
        context['question'] = self.question
        context['answer_form'] = QA_forms.AnswerForm()
        question_comment_forms = []
        for answer in self.question.answer_set:
            question_comment_forms.append(QA_forms.QuestionCommentForm())
        form = MyForm(initial={'ids': [o.id for o in queryset]})
        context['question_comment'] = QA_forms.QuestionCommentForm()
        context['answer_comment'] = QA_forms.AnswerCommentForm()
        context['tag_form'] = QA_forms.TagForm()
        return context

    def post(self, *args, **kwargs):
        if 'answer_form' in self.request.POST:
            answer_form = QA_forms.AnswerForm(self.request.POST)
            answer = answer_form.save()
            request.POST.getlist('ids')
        elif 'question_comment' in self.request.POST:
            pass
        elif 'answer_comment' in self.request.POST:
            pass
        return redirect('view_question', self.question.id)


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

