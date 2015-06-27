from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/user_list.html'


def show_user(request, user_id):
    user = User.objects.get(pk=user_id)
    questions = user.question_set.all()
    return render(request,
                  "users/user.html",
                  {"user": user,
                   "questions": questions})
