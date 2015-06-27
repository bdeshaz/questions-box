
def view_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            sometext = "You have sucessfully logged in, {}!".format(user.username)
            messages.add_message(request, messages.SUCCESS, sometext)
            return redirect('index')
        else:
            return render(request, "Rater/login.html",
                        {"failed": True, "username": username} )
    else:
        user_form = LoginForm()
        return render(request, "Rater/login.html", {'form':user_form})
