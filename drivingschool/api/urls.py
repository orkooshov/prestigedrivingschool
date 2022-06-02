from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from drivingschool.api import views as v

router = routers.DefaultRouter()
router.register('user', v.UserViewSet)
router.register('group', v.GroupViewSet, 'group')
router.register('car', v.CarViewSet)
router.register('schedule-theory', v.ScheduleTheoryViewSet)
router.register('schedule-practice', v.SchedulePracticeStudentViewSet,
    'schedule_practice')
router.register('tutor', v.TutorViewSet)
router.register('instructor', v.InstructorViewSet)
router.register('student', v.StudentViewSet)

urlpatterns = [
    path('', include(router.urls), name='api'),
    path('get-token/', views.obtain_auth_token, name='get_token'),
    path('change-password/', v.ChangePasswordView.as_view())
]