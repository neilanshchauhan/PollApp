from django.contrib import admin
from .models import Question,Choices
# Register your models here.
admin.site.site_header = "PollApp Admin"
admin.site.site_title = "PollApp Admin Area"
admin.site.index_title = "Welcome to PollApp Admin"

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']}),
                 ('Data Info',{'fields':['published'],'classes':['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
