from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = 'M', 'Мужской'
    FEMALE = 'F', 'Женский'

class User(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    phone_number = models.CharField('Телефон', max_length=127, blank=True)
    gender = models.CharField('Пол', max_length=1,
        choices=Gender.choices, blank=True)
    photo = models.ImageField('Фото', blank=True, upload_to='avatars/')
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})
    
    def get_short_name(self) -> str:
        return f'{self.last_name} {self.first_name}'

    def get_full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def is_tutor(self):
        return self.groups.filter(name='Преподаватель').exists()
    
    def get_tutor(self):
        return self.tutor_set.first()

    def is_instructor(self):
        return self.groups.filter(name='Инструктор').exists()

    def is_student(self):
        return self.groups.filter(name='Обучающийся').exists()

    def __str__(self) -> str:
        return self.username
