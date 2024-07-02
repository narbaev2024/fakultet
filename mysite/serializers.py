from rest_framework import serializers
from .models import  Department, Professor, Student, Cours

class DepartmentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ProfessorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class CoursSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'
