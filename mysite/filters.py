from django_filters.rest_framework import FilterSet
from .models import Fakultet, Professor, Student

class ProfessorFilter(FilterSet):
    class Meta:
        model = Professor
        fields = {
            'department': ['exact'],
        }

class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'user': ['exact'],
            'enrollment_date': ['gt', 'lt'],
            'graduation_date': ['gt', 'lt']
        }



class FakultetFilter(FilterSet):
    class Meta:
        model = Fakultet
        fields = {
            'description': ['exact'],
        }

