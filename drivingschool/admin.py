from django.contrib import admin
from . import models as m


class CabinetAdmin(admin.ModelAdmin):
    exclude = ('id', )


class TutorAdmin(admin.ModelAdmin):
    exclude = ('id', )


class GroupAdmin(admin.ModelAdmin):
    exclude = ('id', )


class TopicTheoryAdmin(admin.ModelAdmin):
    exclude = ('id', )

class TopicPracticeAdmin(admin.ModelAdmin):
    exclude = ('id', )

class LessonTheoryAdmin(admin.ModelAdmin):
    exclude = ('id', )

class ScheduleTheoryAdmin(admin.ModelAdmin):
    exclude = ('id', )

class CarBrandAdmin(admin.ModelAdmin):
    exclude = ('id', )

class CarModelAdmin(admin.ModelAdmin):
    exclude = ('id', )

class CarTransmissionAdmin(admin.ModelAdmin):
    exclude = ('id', )

class CarAdmin(admin.ModelAdmin):
    exclude = ('id', )
class InstructorAdmin(admin.ModelAdmin):
    exclude = ('id', )

class StudentAdmin(admin.ModelAdmin):
    exclude = ('id', )

class SchedulePracticeAdmin(admin.ModelAdmin):
    exclude = ('id', )

class LessonPracticeAdmin(admin.ModelAdmin):
    exclude = ('id', )

admin.site.register(m.Cabinet, CabinetAdmin)
admin.site.register(m.Tutor, TutorAdmin)
admin.site.register(m.Group, GroupAdmin)
admin.site.register(m.TopicTheory, TopicTheoryAdmin)
admin.site.register(m.TopicPractice, TopicPracticeAdmin)
admin.site.register(m.LessonTheory, LessonTheoryAdmin)
admin.site.register(m.ScheduleTheory, ScheduleTheoryAdmin)
admin.site.register(m.CarBrand, CarBrandAdmin)
admin.site.register(m.CarModel, CarModelAdmin)
admin.site.register(m.Car, CarAdmin)
admin.site.register(m.Instructor, InstructorAdmin)
admin.site.register(m.Student, StudentAdmin)
admin.site.register(m.SchedulePractice, SchedulePracticeAdmin)
admin.site.register(m.LessonPractice, LessonPracticeAdmin)