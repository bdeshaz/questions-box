from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from qa.models import Answer


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'answers'
    the_user = None

    def dispatch(self, *args, **kwargs):
        self.the_user = User.objects.get(pk=kwargs['pk'])
        return super(UserDetailView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return User.objects.select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answers"] = self.the_user.answer_set.all()
        context["questions"] = self.the_user.question_set.all()
        context["user"] = self.the_user

        return context
