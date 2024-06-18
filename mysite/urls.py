from django.urls import path
from .views import FakultetViewSet, ProfessorViewSet, CourseViewSet


urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='course_detail'),
    path('', FakultetViewSet.as_view({'get': 'list', 'post': 'create'}), name='name_list'),
    path('<int:pk>/', FakultetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
    path('', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),
]