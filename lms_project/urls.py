# lms_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('about_course/', about_course, name='about_course'),
    path('about_platform/', about_platform, name='about_platform'),
    path('student/<int:student_id>/', student_dashboard, name='student_dashboard'),
    path('teacher/<int:teacher_id>/', teacher_dashboard, name='teacher_dashboard'),
    path('prorector/', prorector_dashboard, name='prorector_dashboard'),
    path('prorector_teachers/', prorector_teacher, name='prorector_teacher'),
    path('prorector_students/', prorector_student, name='prorector_student'),
    path('prorector_course/', prorector_course, name='prorector_course'),
    path('add_course/', add_course, name='add_course'),  # Добавление курса
    path('create_course/', create_course, name='create_course'),  # Добавление курса
    path('edit_course/<int:course_id>/', edit_course, name='edit_course'),  # Редактирование курса
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),  # Удаление курса
    path('prorector_assignment/<int:course_id>/', prorector_assignment, name='prorector_assignment'),  # Задания для курса
    path('add_assignment/<int:course_id>/', add_assignment, name='add_assignment'),  # Добавление задания
    path('edit_assignment/<int:assignment_id>/', edit_assignment, name='edit_assignment'),  # Редактирование задания
    path('delete_assignment/<int:assignment_id>/', delete_assignment, name='delete_assignment'),  # Удаление задания
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('edit_teacher/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('add_student/', add_student, name='add_student'),
    path('edit_student/<int:student_id>/', edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('student_assignment/<int:course_id>/', student_assignment, name='student_assignment'),  # Задания для курса у студента
]

