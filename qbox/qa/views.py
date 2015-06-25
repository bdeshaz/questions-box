from django.shortcuts import render
import django.views.generic as django_views
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Question, Answer, Tag, Comment

# Create your views here.

class QuestionDetailView(django_views.ListView):
    template_name = 'question.html'
    model=models.Answer
    context_object_name='answers'
    paginate_by=30
	self.question = None

	def dispatch(self, *args, **kwargs):
		self.question = Question.objects.get(pk=self.kwargs['pk'])
		return super(QuestionDetailView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		return self.question.answer_set.order_by('-posted_at')

	def get_context_data(self, **kwargs):
		context = super(QuestionDetailView, self).get_context_data(**kwargs)
		context['question'] = self.question
		return context
