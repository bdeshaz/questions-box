from django import forms
from .models import Question, Tags, Comment, Answers


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ('text',)