from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from . import models as m
from .forms import CustomUserCreationForm, CustomUserChangeForm


class DefaultAdmin(admin.ModelAdmin):
    exclude = ('id', )


class TutorAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'cabinet']


class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'is_active',
                    'last_name', 'first_name', 'middle_name', 'gender',)
    list_filter = ('groups', 'is_active', 'is_superuser', 'gender',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'phone_number',
         'first_name', 'last_name', 'middle_name', 'gender', 'photo')}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions',)}),
        (_('Additional info'), {'fields': ('last_login', 'date_joined',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',)}
         ),
        (_('Permissions'), {
            'fields': ('is_superuser', 'is_staff', 'groups')
        })
    )
    search_fields = ('username', 'email', 'last_name', 'first_name')
    ordering = ('last_name', 'first_name')


admin.site.register(
    (
        m.Cabinet, m.Group, m.TopicTheory, m.TopicPractice, m.LessonTheory,
        m.LessonPractice, m.ScheduleTheory, m.SchedulePractice, m.Car,
        m.CarBrand, m.CarModel, m.Student, m.Mark, m.CallApplication
    ), DefaultAdmin)
admin.site.register(m.Tutor, TutorAdmin)
admin.site.register(m.Instructor, InstructorAdmin)
admin.site.register(m.User, CustomUserAdmin)
