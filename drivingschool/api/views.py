from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework import status

from drivingschool.api import serializers as s
from drivingschool import models as m


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]
    serializer_class = s.UserSerializer
    queryset = m.User.objects.all().order_by('pk')


class ChangePasswordView(UpdateAPIView):
    serializer_class = s.ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # if using drf authtoken, create a new token 
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        token, created = Token.objects.get_or_create(user=user)
        # return new token
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class TutorViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.TutorSerializer
    queryset = m.Tutor.objects.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.GroupSerializer
    queryset = m.Group.objects.all()


class ScheduleTheoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.GroupScheduleTheorySerializer
    queryset = m.Group.objects.all()


class SchedulePracticeStudentViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'user__username'
    permission_classes = [IsAuthenticated]
    serializer_class = s.SchedulePracticeStudentSerializer
    queryset = m.Student.objects.all().select_related('user')


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.CarSerializer
    queryset = m.Car.objects.all()


class InstructorViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = s.InstructorSerializer
    queryset = m.Instructor.objects.all()


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'user__username'
    permission_classes = [IsAuthenticated]
    serializer_class = s.StudentSerializer
    queryset = m.Student.objects.all().select_related('user')
