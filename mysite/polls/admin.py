from django.contrib import admin
# from django.polls import models
from polls.models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

# class QuestionAdmin(Model.models)
class QuestionAdmin(admin.ModelAdmin):
    # ('question_text', 'pub_date')
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)