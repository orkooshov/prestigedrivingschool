from rest_framework import viewsets
from drivingschool.api import serializers as s
from drivingschool import models as m


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.UserSerializer
    queryset = m.User.objects.all().order_by('pk')


class TutorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.TutorSerializer
    queryset = m.Tutor.objects.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.GroupSerializer
    queryset = m.Group.objects.all()


class ScheduleTheoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.ScheduleTheorySerializer
    queryset = m.ScheduleTheory.objects.all()


class SchedulePracticeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.SchedulePracticeSerializer
    queryset = m.SchedulePractice.objects.all()


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.CarSerializer
    queryset = m.Car.objects.all()


class InstructorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.InstructorSerializer
    queryset = m.Instructor.objects.all()


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.StudentSerializer
    queryset = m.Student.objects.all()
