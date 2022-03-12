from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Weekday(models.IntegerChoices):
    MONDAY = 0, 'Понедельник'
    TUESDAY = 1, 'Вторник'
    WEDNESDAY = 2, 'Среда'
    THURSDAY = 3, 'Четверг'
    FRIDAY = 4, 'Пятница'
    SATURDAY = 5, 'Суббота'
    SUNDAY = 6, 'Воскресенье'


class Cabinet(models.Model):
    cabinet = models.CharField(max_length=31, verbose_name='Кабинет')

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

    def __str__(self) -> str:
        return self.cabinet


class Tutor(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, 
        verbose_name='Кабинет')
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
        verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self) -> str:
        return f'{self.user.get_full_name()}'


class Group(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, 
        verbose_name='Преподаватель')
    name = models.CharField(max_length=31, verbose_name='Название')

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.name


class TopicTheory(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')

    class Meta:
        verbose_name = 'Тема теоритическая'
        verbose_name_plural = 'Темы теоритические'

    def __str__(self) -> str:
        return self.name


class TopicPractice(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')

    class Meta:
        verbose_name = 'Тема практическая'
        verbose_name_plural = 'Темы практические'

    def __str__(self) -> str:
        return self.name


class LessonTheory(models.Model):
    topic = models.ManyToManyField(TopicTheory, verbose_name='Тема')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, 
        verbose_name='Группа')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, 
        verbose_name='Преподаватель')
    started_at = models.DateTimeField(auto_now=True, verbose_name='Дата начала')

    class Meta:
        verbose_name = 'Занятие теоритическое'
        verbose_name_plural = 'Занятия теоритические'


class ScheduleTheory(models.Model):
    # todo
    group = models.ForeignKey(Group, on_delete=models.CASCADE, 
        verbose_name='Группа')
    weekday = models.IntegerField(choices=Weekday.choices, 
        verbose_name='День недели')

    class Meta:
        verbose_name = 'Расписание теор. занятий'
        verbose_name_plural = 'Расписания теор. занятий'


class CarBrand(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марки авто'

    def __str__(self) -> str:
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модели авто'

    def __str__(self) -> str:
        return self.name


class CarTransmission(models.IntegerChoices):
    MECHANIC = 0, 'Механика'
    AUTOMATIC = 1, 'Автомат'


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, 
        verbose_name='Марка')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, 
        verbose_name='Модель')
    transmission = models.IntegerField(choices=CarTransmission.choices, 
        verbose_name='Коробка передач')
    state_number = models.CharField(max_length=15, verbose_name='Госномер')

    def get_name(self):
        return f'{self.brand} {self.model}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self) -> str:
        return self.state_number


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Авто')

    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструкторы'

    def __str__(self) -> str:
        return self.user.get_full_name()


class LicenseCategory(models.TextChoices):
    A = 'А'
    B = 'Б'
    C = 'В'
    D = 'Г'
    E = 'Д'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
        verbose_name='Пользователь')
    license_category = models.CharField(choices=LicenseCategory.choices, 
        max_length=1, verbose_name='Категория прав')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, 
        verbose_name='Группа')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE,
        verbose_name='Инструктор')

    def __str__(self) -> str:
        return str(self.user)

    class Meta:
        verbose_name = 'Обучающийся'
        verbose_name_plural = 'Обучающиеся'


class SchedulePractice(models.Model):
    # todo
    weekday = models.IntegerField(choices=Weekday.choices, 
        verbose_name='День недели')
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
        verbose_name='Обучающийся')
    
    class Meta:
        verbose_name = 'Расписание прак. занятий'
        verbose_name_plural = 'Расписания прак. занятий'


class LessonPractice(models.Model):
    topic = models.ManyToManyField(TopicPractice, verbose_name='Тема')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, 
        verbose_name='Обучающийся')
    started_at = models.DateTimeField(blank=True, verbose_name='Дата начала')

    class Meta:
        verbose_name = 'Занятие практическое'
        verbose_name_plural = 'Занятия практические'


class MarkDictionary(models.IntegerChoices):
    A = 5, 'Отлично'
    B = 4, 'Хорошо'
    C = 3, 'Удовлетворительно'
    D = 2, 'Неудовлетворительно'
    E = 1, 'Кол'


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
        verbose_name='Обучающийся')
    mark = models.IntegerField(choices=MarkDictionary.choices,
        verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name='Поставлена')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменена')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class CallApplication(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self) -> str:
        return f'{self.name} {self.phone_number}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'