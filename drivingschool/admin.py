from django.contrib import admin
from . import models as m
from django.utils.translation import gettext as _


class DefaultAdmin(admin.ModelAdmin):
    exclude = ('id', )


class TutorAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'cabinet']


admin.site.register(
    (
        m.Cabinet, m.Group, m.TopicTheory, m.TopicPractice, m.LessonTheory, 
        m.LessonPractice, m.ScheduleTheory, m.SchedulePractice, m.Car,
        m.CarBrand, m.CarModel, m.Instructor, m.Student
    ), DefaultAdmin)
admin.site.register(m.Tutor, TutorAdmin)
