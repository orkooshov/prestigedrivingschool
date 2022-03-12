from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (authenticate, login as dj_login,
    logout as dj_logout)
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic import (TemplateView, RedirectView, DetailView, 
    FormView, CreateView, UpdateView, DeleteView, ListView)

from drivingschool import models as m
from drivingschool.decorators import *


def home(request):
    return render(request, 'drivingschool/home.html')

def logout(request):
    dj_logout(request)
    return redirect('home')

def whoami(request):
    return HttpResponse(str(request.user))

def about_us(request):
    return HttpResponse('About Us')

def contact_us(request):
    return HttpResponse('Contact Us')

def pricing(request):
    return HttpResponse('Pricing')

def call_application(request):
    m.CallApplication.objects.create(
        name=request.POST.get('name').strip(), 
        phone_number = request.POST.get('phone_number').strip()
    )
    return HttpResponse('Call Application')

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
    context = {
        'user': request.user,
        'student': m.Student.objects.filter(user=request.user).first()
    }
    return render(request, 'drivingschool/student.html', context)


class GroupListView(ListView):
    queryset = m.Group.objects.all()

class GroupDetailView(DetailView):
    model = m.Group

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'drivingschool/user_detail.html'