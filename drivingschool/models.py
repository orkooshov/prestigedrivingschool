from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Weekday(models.IntegerChoices):
    MONDAY = 0, _('Monday')
    TUESDAY = 1, _('Tuesday')
    WEDNESDAY = 2, _('Wednesday')
    THURSDAY = 3, _('Thursday')
    FRIDAY = 4, _('Friday')
    SATURDAY = 5, _('Saturday')
    SUNDAY = 6, _('Sunday')


class Cabinet(models.Model):
    cabinet = models.CharField(_('cabinet'), max_length=31)

    def __str__(self) -> str:
        return self.cabinet


class Tutor(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.get_full_name()}'


class Group(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    name = models.CharField(max_length=31)

    def __str__(self) -> str:
        return self.name


class TopicTheory(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name


class TopicPractice(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name


class LessonTheory(models.Model):
    topic = models.ManyToManyField(TopicTheory)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now=True)


class ScheduleTheory(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=Weekday.choices)


class CarBrand(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name


class CarTransmission(models.IntegerChoices):
    MECHANIC = 0, _('Mechanic')
    AUTOMATIC = 1, _('Automatic')


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    transmission = models.IntegerField(choices=CarTransmission.choices)
    state_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.state_number


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.get_full_name()


class LicenseCategory(models.TextChoices):
    A = 'А'
    B = 'Б'
    C = 'В'
    D = 'Г'
    E = 'Д'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_category = models.CharField(choices=LicenseCategory.choices, max_length=1)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)


class SchedulePractice(models.Model):
    weekday = models.IntegerField(choices=Weekday.choices)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class LessonPractice(models.Model):
    topic = models.ManyToManyField(TopicPractice)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    started_at = models.DateTimeField(blank=True)
