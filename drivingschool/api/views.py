from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from drivingschool.api import serializers as s
from drivingschool import models as m


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.UserSerializer
    queryset = m.User.objects.all().order_by('pk')


class TutorViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.TutorSerializer
    queryset = m.Tutor.objects.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.GroupSerializer
    queryset = m.Group.objects.all()


# class ScheduleTheoryViewSet(viewsets.ReadOnlyModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = s.ScheduleTheorySerializer
#     queryset = m.ScheduleTheory.objects.all()


class ScheduleTheoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.GroupScheduleTheorySerializer
    queryset = m.Group.objects.all()


class SchedulePracticeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.SchedulePracticeSerializer
    queryset = m.SchedulePractice.objects.all()


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.CarSerializer
    queryset = m.Car.objects.all()


class InstructorViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.InstructorSerializer
    queryset = m.Instructor.objects.all()


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.StudentSerializer
    queryset = m.Student.objects.all()
