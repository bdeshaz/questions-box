from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from .forms import UserForm


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
        context["score"] = (
            sum(num.score() for num in self.the_user.answer_set.all()) +
            (self.the_user.question_set.count() * 5) +
            (self.the_user.answerdownvote_set.count() * -1)
        )

        return context


class UserListView(generic.ListView):
    model=User
    template_name='users/user_list.html'
    context_object_name='users'
    paginate_by=30

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        print(context)
        for i in range(len(context['users'])):
            usr = context['users'][i]
            context['users'][i].print_score = (
                sum(num.score() for num in usr.answer_set.all()) +
                (usr.question_set.count() * 5) +
                (usr.answerdownvote_set.count() * -1)
            )
        # for
        # context["score"] = (
        #     sum(num.score() for num in self.the_user.answer_set.all()) +
        #     (self.the_user.question_set.count() * 5) +
        #     (self.the_user.answerdownvote_set.count() * -1)
        # context['question'] = self.question
        # context['form'] = QA_forms.TagForm()
        return context


@login_required
def edit_user(request):
    user = request.user
    if request.method == "GET":
        user_form = UserForm(instance=user)
    elif request.method == "POST":
        user_form = UserForm(instance=user, data=request.POST)
        if user_form.is_valid():
            n_user = user_form.save()
            password = user.password
            n_user.set_password(password)
            n_user.save()
            n_user = authenticate(username=n_user.username,
                                  password=password)
            login(request, n_user)
            messages.add_message(request, messages.SUCCESS,
                                 "Your profile has been updated!")
            return redirect('/questions/')

    return render(request, "users/edit_user.html", {"form": user_form})
