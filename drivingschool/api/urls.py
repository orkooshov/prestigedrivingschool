from django.urls import path, include
from rest_framework import routers

from drivingschool.api import views as v

router = routers.DefaultRouter()
router.register('user', v.UserViewSet)
router.register('group', v.GroupViewSet)
router.register('car', v.CarViewSet)
router.register('schedule-theory', v.ScheduleTheoryViewSet)
router.register('schedule-practice', v.SchedulePracticeViewSet)
router.register('tutor', v.TutorViewSet)
router.register('instructor', v.InstructorViewSet)
router.register('student', v.StudentViewSet)

urlpatterns = [
    path('', include(router.urls), name='api'),
]