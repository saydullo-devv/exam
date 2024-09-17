from django.contrib import admin
from .models import Group, Student, Subject, Exam, Question, Option, Price

# admin.site.register(Group)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'group', )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'time', )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'exam', )

Price
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'option', )
