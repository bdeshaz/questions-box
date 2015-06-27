from django import forms
from .models import Question, Tag, Comment, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')

class QuestionCommentForm(forms.ModelForm):
    class Meta:
        model = QuestionComment
        fields = ('text', )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)

class AnswerCommentForm(forms.ModelForm):
    class Meta:
        model = AnswerComment
        fields = ('text',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('text',)
