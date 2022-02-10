from django.contrib import admin
from . import models as m
from django.utils.translation import gettext as _


class DefaultAdmin(admin.ModelAdmin):
    exclude = ('id', )


class TutorAdmin(admin.ModelAdmin):
    # exclude = ('id', )
    list_display = ['id', '__str__', 'cabinet']


admin.site.register(m.Cabinet, DefaultAdmin)
admin.site.register(m.Tutor, TutorAdmin)
admin.site.register(m.Group, DefaultAdmin)
admin.site.register(m.TopicTheory, DefaultAdmin)
admin.site.register(m.TopicPractice, DefaultAdmin)
admin.site.register(m.LessonTheory, DefaultAdmin)
admin.site.register(m.ScheduleTheory, DefaultAdmin)
admin.site.register(m.CarBrand, DefaultAdmin)
admin.site.register(m.CarModel, DefaultAdmin)
admin.site.register(m.Car, DefaultAdmin)
admin.site.register(m.Instructor, DefaultAdmin)
admin.site.register(m.Student, DefaultAdmin)
admin.site.register(m.SchedulePractice, DefaultAdmin)
admin.site.register(m.LessonPractice, DefaultAdmin)