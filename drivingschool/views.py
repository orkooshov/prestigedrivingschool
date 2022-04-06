from typing import Any, Dict
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.auth import (authenticate, login as dj_login,
    logout as dj_logout)
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic import (DetailView, ListView)
from rest_framework import viewsets

from drivingschool import models as m
from drivingschool.decorators import *
from drivingschool.forms import EditPersonalInfoForm
from drivingschool import serializers as s

def user_edit(request):
    form = EditPersonalInfoForm(instance=request.user)
    if request.method == 'POST':
        form = EditPersonalInfoForm(data=request.POST, 
            files=request.FILES, 
            instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, 'drivingschool/user_edit.html', 
        {'form': form})

def home(request):
    context = {
        'header_selected_index': 0
    }
    return render(request, 'drivingschool/home.html', context)

def logout(request):
    dj_logout(request)
    return redirect('home')

def whoami(request):
    return HttpResponse(str(request.user))

def about_us(request):
    context = {
        'header_selected_index': 2
    }
    return render(request, 'drivingschool/about_us.html', context)

def contact_us(request):
    context = {
        'header_selected_index': 3
    }
    return render(request, 'drivingschool/contact_us.html', context)

def pricing(request):
    context = {
        'header_selected_index': 1
    }
    return render(request, 'drivingschool/pricing.html', context)

def call_application(request):
    if request.method == 'POST':
        m.CallApplication.objects.create(
            name=request.POST.get('name').strip(), 
            phone_number = request.POST.get('phone_number').strip()
        )
        return HttpResponse('Заявка отправлена')
    raise Http404

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('student')
        return render(request, 'drivingschool/login.html')

    def post(self, request, *args, **kwargs):
        user = authenticate(request,
            username=request.POST.get('username', ''),
            password=request.POST.get('password', ''))
        if user is None:
            return HttpResponse('Неверный логин или пароль')
        dj_login(request, user)
        if user.is_tutor():
            return redirect('tutor')
        if user.is_instructor():
            return redirect('instructor')
        if user.is_student():
            return redirect('student')
        return HttpResponse('хз')


def tutor_view(request):
    return HttpResponse('teacher')

def instructor_view(request):
    return HttpResponse('фдываолфдыао')

@login_required
def student_view(request):
    return render(request, 'drivingschool/student.html')


class GroupListView(ListView):
    queryset = m.Group.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_selected_index'] = 0
        return context

class GroupDetailView(DetailView):
    model = m.Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_selected_index'] = 0
        return context

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'drivingschool/user_detail.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(context['user'].username)
        return context


class SchedulePracticeListView(ListView):
    model = m.SchedulePractice
    template_name = 'drivingschool/schedule_practice_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_selected_index'] = 2
        return context


class ScheduleTheoryListView(ListView):
    model = m.Group
    template_name = 'drivingschool/schedule_theory_list.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_selected_index'] = 1
        return context

class InstructorListView(ListView):
    model = m.Instructor
    context_object_name = 'instructors'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_selected_index'] = 3
        return context



############# DRF ################
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