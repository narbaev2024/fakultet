from rest_framework import serializers
from .models import  Fakultet, Professor, Student, Course, Cabinet, Raspisanie, Zapis_na_course,Dz, Sdacha_dz

class FakultetSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = '__all__'


class ProfessorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CabinetSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'


class RaspisanieSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Raspisanie
        fields = '__all__'


class Zapis_na_courseSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Zapis_na_course
        fields = '__all__'


class DzSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Dz
        fields = '__all__'


class Sdacha_dzSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Sdacha_dz
        fields = ['assigment', 'student', 'submission_date', 'grade', 'feedback']