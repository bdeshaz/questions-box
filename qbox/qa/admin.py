from django.contrib import admin
from qa.models import Tag, Comment, Answer, Question


class TagAdmin(admin.ModelAdmin):
    list_display = ['text']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'posted_at', 'score', 'owner']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'posted_at', 'score', 'owner']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['parent_question']

# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
