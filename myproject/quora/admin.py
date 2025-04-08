from django.contrib import admin
from .models import Question, Answer, Like

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'created_at')
    search_fields = ('text', 'user__username')
    list_filter = ('created_at',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'text', 'user', 'created_at')
    search_fields = ('text', 'user__username', 'question__text')
    list_filter = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'user', 'created_at')
    search_fields = ('user__username', 'answer__text')
    list_filter = ('created_at',)
