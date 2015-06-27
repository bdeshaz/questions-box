
def view_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    rs = movie.rating_set.order_by('-posted')[:200]
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        new_rating = request.POST.get('rating')
        new_review = request.POST.get('review')
        user = request.user
        r = Rating(rater=user.rater, movie=movie, rating=new_rating, review=new_review)
        dt_now = datetime.datetime.now()
        post_int = (dt_now - datetime.datetime(1970, 1, 1)).total_seconds()
        r.posted = post_int
        r.save()
        movie.update_store(new_rating)
        sometext = "You have rated this movie {} stars, ".format(new_rating)
        sometext += "{}.".format(user.username)
        messages.add_message(request, messages.SUCCESS, sometext)
#        return redirect('view_movie')
        return render(request,
                  "Rater/movie.html",
                  {"movie": movie, "ratings": rs, "user_rate": True,
                   "rating_form": rating_form, "star_hist": movie.star_hist() })
    else:
        rating_form = RatingForm()
        user = request.user
        if user is not None and user.is_authenticated():
            user_rate = user.rater.has_rated(movie)
        else:
            user_rate = False
        return render(request,
                      "Rater/movie.html",
                      {"movie": movie, "ratings": rs, "user_rate": user_rate,
                       "rating_form": rating_form })
