from django.shortcuts import render
import django.views.generic as django_views
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from qa.models import Question, Answer, Tag, Comment
import qa.forms as QA_forms

# Create your views here.

class QuestionDetailView(django_views.ListView):
    template_name = 'question.html'
    model = Answer
    context_object_name='answers'
    paginate_by=30
    question = None

    def dispatch(self, *args, **kwargs):
        self.question = Question.objects.get(pk=self.kwargs['pk'])
        return super(QuestionDetailView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.question.answer_set.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['question'] = self.question
        context['answer_form'] = QA_forms.AnswerForm
        return context

    def post(self, *args, **kwargs):
        answer_form = QA_forms.AnswerForm(self.request.POST)
        answer = answer_form.save()
        return render(request, self.template_name)

class AskQuestionView(django_views.edit.CreateView): #or FormView
    model = Question
    template_name = "ask.html"
    fields = ["title", "text", "score"]
    # success_url = 'http://www.google.com'

    def form_valid(self, form):
        question = form.save(commit=False)
        question.score = 0
        question.owner = self.request.user
        return super(AskQuestionView, self).form_valid(form)
        question.save()

