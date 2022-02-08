from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')

class User(AbstractUser):
    middle_name = models.CharField(_('Middle name'), max_length=150, blank=True)
    phone_number = models.CharField(_('Phone number'), max_length=127, blank=True)
    gender = models.CharField(max_length=1,
        choices=Gender.choices, blank=True)
    photo = models.ImageField(_('Avatar'), width_field=300, height_field=300, 
        blank=True)
    
    def get_short_name(self) -> str:
        return f'{self.last_name} {self.first_name}'

    def get_full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def __str__(self) -> str:
        return self.username
