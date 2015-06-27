
class ClickView(views.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'click_view_redirect'
    url = 'http://www.google.com' # if approach fails

    def get_redirect_url(self, *args, **kwargs):
        bookmark = Bookmark.objects.get(code=kwargs['code'])
#        user = request.user
#        if user is not None:
#            click = Click(bookmark=bookmark, user=user)
#        else:
        click = Click(bookmark=bookmark)
        click.set_time()
        click.save()
        self.url = bookmark.URL
        return super(ClickView, self).get_redirect_url(*args, **kwargs)
