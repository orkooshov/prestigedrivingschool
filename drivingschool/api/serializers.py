from cProfile import label
from rest_framework import serializers
from drivingschool import models as m


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.User
        fields = ['id', 'username', 'email', 'gender',
                  'phone_number', 'groups', 'photo']


class TutorSerializer(serializers.ModelSerializer):
    cabinet = serializers.StringRelatedField()
    user = UserSerializer()

    class Meta:
        model = m.Tutor
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer()

    class Meta:
        model = m.Group
        fields = '__all__'


class ScheduleTheorySerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()

    def get_position(self, instance):
        return instance.get_position_display()

    class Meta:
        model = m.ScheduleTheory
        fields = '__all__'


class GroupScheduleTheorySerializer(serializers.ModelSerializer):
    schedule_theory = ScheduleTheorySerializer(
        many=True, source='scheduletheory_set')

    class Meta:
        model = m.Group
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    model = serializers.StringRelatedField()
    transmission = serializers.SerializerMethodField()

    def get_transmission(self, instance):
        return instance.get_transmission_display()

    class Meta:
        model = m.Car
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = CarSerializer()

    class Meta:
        model = m.Instructor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    group = GroupSerializer()
    instructor = InstructorSerializer()

    class Meta:
        model = m.Student
        fields = '__all__'


class SchedulePracticeSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    weekday = serializers.SerializerMethodField()

    def get_position(self, instance):
        return instance.get_position_display()
    def get_weekday(self, instance):
        return instance.get_weekday_display()

    class Meta:
        model = m.SchedulePractice
        fields = '__all__'
