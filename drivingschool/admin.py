from django.contrib import admin
from . import models as m
from django.utils.translation import gettext as _


class DefaultAdmin(admin.ModelAdmin):
    exclude = ('id', )


class TutorAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'cabinet']

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']


admin.site.register(
    (
        m.Cabinet, m.Group, m.TopicTheory, m.TopicPractice, m.LessonTheory, 
        m.LessonPractice, m.ScheduleTheory, m.SchedulePractice, m.Car,
        m.CarBrand, m.CarModel, m.Student, m.Mark, m.CallApplication
    ), DefaultAdmin)
admin.site.register(m.Tutor, TutorAdmin)
admin.site.register(m.Instructor, InstructorAdmin)
