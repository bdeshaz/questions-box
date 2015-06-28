from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from qa.models import Answer


class QuestionDetailView(generic.DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'answers'

    def get_queryset(self):
        return User.objects.select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answers"] = self.request.user.answer_set.all()
        context["questions"] = self.request.user.question_set.all()
        context

        return context
