from django import forms
from qa import models
from django.forms.widgets import MultipleHiddenInput


class QuestionForm(forms.ModelForm):
    ids = forms.MultipleChoiceField(widget=MultipleHiddenInput())
    # http://stackoverflow.com/questions/2701303/multiplehiddeninput-doesnt-encode-properly-over-post
    class Meta:
        model = models.Question
        fields = ('title', 'text')

class QuestionCommentForm(forms.ModelForm):
    class Meta:
        model = models.QuestionComment
        fields = ('text', )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ('text',)

class AnswerCommentForm(forms.ModelForm):
    answer_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = models.AnswerComment
        fields = ('text', 'answer_id', )

class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ('text',)

# other approaches for array input
# from django.contrib.postgres.forms import SimpleArrayField
#     tags = SimpleArrayField(forms.CharacterField(max_length=255))
    # https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/forms/#simplearrayfield
