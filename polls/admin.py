from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['question_text']}),
        ('Date info', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date')
    #fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
# Register your models here.
