from django.contrib import admin
from qa import models


class TagAdmin(admin.ModelAdmin):
    list_display = ['text']

class AnswerCommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'posted_at', 'owner']

class QuestionCommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'posted_at']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'posted_at', 'score', 'owner']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['parent', 'posted_at', 'text', 'owner']

# upvotes
class QuestionUpvoteAdmin(admin.ModelAdmin):
    list_display = ['posted_at', 'parent', 'voter']

# Register your models here.
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.AnswerComment, AnswerCommentAdmin)
admin.site.register(models.QuestionComment, QuestionCommentAdmin)
admin.site.register(models.Answer, AnswerAdmin)
admin.site.register(models.Question, QuestionAdmin)

admin.site.register(models.QuestionUpvote, QuestionUpvoteAdmin)
