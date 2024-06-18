from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Fakultet, Professor, Student, Course, Cabinet, Raspisanie, Zapis_na_course,Dz, Sdacha_dz
from .serializers import FakultetSerialzer, ProfessorSerialzer, StudentSerialzer, CourseSerialzer, CabinetSerialzer, RaspisanieSerialzer, Zapis_na_courseSerialzer, DzSerialzer, Sdacha_dzSerialzer
from rest_framework.filters import SearchFilter
from .filters import  ProfessorFilter, FakultetFilter, StudentFilter

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerialzer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerialzer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProfessorFilter
    search_fields = ['user']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['user']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FakultetViewSet(viewsets.ModelViewSet):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerialzer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = FakultetFilter
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerialzer

class RaspisanieViewSet(viewsets.ModelViewSet):
        queryset = Raspisanie.objects.all()
        serializer_class = RaspisanieSerialzer



class Zapis_na_courseViewSet(viewsets.ModelViewSet):
    queryset = Zapis_na_course.objects.all()
    serializer_class = Zapis_na_courseSerialzer


class DzViewSet(viewsets.ModelViewSet):
    queryset = Dz.objects.all()
    serializer_class = DzSerialzer

class Sdacha_dzViewSet(viewsets.ModelViewSet):
    queryset = Sdacha_dz.objects.all()
    serializer_class = Sdacha_dzSerialzer




