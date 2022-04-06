from unicodedata import name
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from drivingschool import views as v

router = routers.DefaultRouter()
router.register('user', v.UserViewSet)
router.register('tutor', v.TutorViewSet)
router.register('group', v.GroupViewSet)
router.register('schedule-theory', v.ScheduleTheoryViewSet)
router.register('schedule-practice', v.SchedulePracticeViewSet)
router.register('car', v.CarViewSet)
router.register('instructor', v.InstructorViewSet)
router.register('student', v.StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('', v.home, name='home'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.logout, name='logout'),
    path('whoami/', v.whoami),
    path('student/', v.student_view, name='student'),
    path('instructor/', v.instructor_view, name='instructor'),
    path('tutor/', v.tutor_view, name='tutor'),
    path('about/', v.about_us, name='about_us'),
    path('contact/', v.contact_us, name='contact_us'),
    path('pricing/', v.pricing, name='pricing'),
    path('call-application/', v.call_application, name='call_application'),
    path('group/<int:pk>/', v.GroupDetailView.as_view(), name='group_detail'),
    path('groups/', v.GroupListView.as_view(), name='group_list'),
    path('user/<slug:username>/', v.UserDetailView.as_view(), name='user_detail'),
    path('schedule-theory/', v.ScheduleTheoryListView.as_view(), 
        name='schedule_theory_list'),
    path('schedule-practice/', v.SchedulePracticeListView.as_view(), 
        name='schedule_practice_list'),
    path('instructors/', v.InstructorListView.as_view(), name='instructor_list'),
    path('user-edit/', v.user_edit, name='user_edit'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)