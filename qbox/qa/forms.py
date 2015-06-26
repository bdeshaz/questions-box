from django import forms
from .models import Question, Tag, Comment, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('text',)
