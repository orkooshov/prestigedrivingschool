from drivingschool import models as m
import random as r
import string

male_names = (
    'Тимофей',
    'Роман',
    'Владимир',
    'Иван',
    'Кирилл',
    'Михаил',
    'Ярослав',
    'Павел',
    'Егор',
    'Георгий',
)
male_surnames = (
    'Коротков',
    'Урбановский',
    'Руснак',
    'Кузьмич',
    'Бабурин',
    'Пушной',
    'Цыркунов',
    'Дворянкин',
    'Агабабян',
)

class Test:
    @staticmethod
    def create_user():
        username = ''.join(r.choice(string.ascii_lowercase) for _ in range(5))
        password = '12345678Privet'
        email = username + '@gmail.com'
        first_name = r.choice(male_names)
        last_name = r.choice(male_surnames)
        gender = m.Gender.MALE

        user = m.User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender
        )
        # user.save()
        return user

    @staticmethod
    def create_student(user):
        lc = m.LicenseCategory.B
        group = m.Group.objects.order_by('?').first()
        instructor = m.Instructor.objects.order_by('?').first()
        student = m.Student.objects.create(
            user=user,
            license_category=lc,
            group=group,
            instructor=instructor
        )
        # student.save()
        return student

for _ in range(10):
    user = Test.create_user()
    user.save()
    st = Test.create_student(user)
    st.save()
    # print(user.username)
    # print(user.password)
    # print(user.email)
    # print(user.first_name)
    # print(user.last_name)
    print(st.instructor)
