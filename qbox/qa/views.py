from django.shortcuts import render
import django.views.generic as django_views
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Question, Answer, Tag, Comment

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
        return context

class AskQuestionView(django_views.edit.CreateView): #or FormView
    model = Question
    template_name = "ask.html"
    fields = ["title", "text"]

    def form_valid(self, form):
        question = form.save()
        question.owner = request.user
        question.save()
        return super(AskQuestionView, self).form_valid(form)
