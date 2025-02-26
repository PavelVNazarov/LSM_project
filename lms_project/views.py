# lms_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import People, Course, Assignment
from .forms import CourseForm, AssignmentForm

def home(request):
    return render(request, 'home.html')

def about_course(request):
    return render(request, 'about_course.html')

def about_platform(request):
    return render(request, 'about_platform.html')

def login_view(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if login == 'superadmin' and password == '1234':
            return redirect('prorector_dashboard')
        try:
            user = People.objects.get(login=login)
            if user.password == password:
                role = user.role
                if role == 'student':
                    return redirect('student_dashboard', student_id=user.id)  # Передаем ID студента
                elif role == 'teacher':
                    return redirect('teacher_dashboard', teacher_id=user.id)  # Передаем ID преподавателя
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
        except People.DoesNotExist:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'login.html')

def add_teacher(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        People.objects.create(login=login, name=name, email=email, password=password, role='teacher')
        return redirect('prorector_dashboard')
    return render(request, 'add_teacher.html')

def edit_teacher(request, teacher_id):
    user = get_object_or_404(People, id=teacher_id, role='teacher')
    if request.method == 'POST':
        user.login = request.POST['login']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.name = request.POST['name']
        user.role = request.POST['role']
        user.save()
        return redirect('prorector_dashboard')
    return render(request, 'edit_teacher.html', {'teacher': user})

def add_student(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        People.objects.create(login=login, name=name, email=email, password=password, role='student')
        return redirect('prorector_dashboard')
    return render(request, 'add_student.html')

def edit_student(request, student_id):
    user = get_object_or_404(People, id=student_id, role='student')
    if request.method == 'POST':
        user.login = request.POST['login']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.name = request.POST['name']
        user.role = request.POST['role']
        user.save()
        return redirect('prorector_dashboard')
    return render(request, 'edit_student.html', {'student': user})

def delete_student(request, student_id):
    people = get_object_or_404(People, id=student_id, role='student')
    people.delete()
    return redirect('prorector_dashboard')

def delete_teacher(request, teacher_id):
    people = get_object_or_404(People, id=teacher_id, role='teacher')
    people.delete()
    return redirect('prorector_dashboard')

def prorector_teacher(request):
    teachers = People.objects.filter(role='teacher')
    return render(request, 'prorector_teacher.html', {'teachers': teachers})

def prorector_student(request):
    students = People.objects.filter(role='student')
    return render(request, 'prorector_student.html', {'students': students})

def student_dashboard(request, student_id):
    student = get_object_or_404(People, id=student_id, role='student')
    courses = Course.objects.all()
    return render(request, 'student_dashboard.html', {'student': student, 'courses': courses})

def teacher_dashboard(request, teacher_id):
    teacher = get_object_or_404(People, id=teacher_id, role='teacher')
    return render(request, 'teacher_dashboard.html', {'teacher': teacher})

def prorector_dashboard(request):
    return render(request, 'prorector_dashboard.html')

def prorector_course(request):
    courses = Course.objects.all()
    return render(request, 'prorector_course.html', {'courses': courses})

def prorector_assignment(request, course_id):
    course = Course.objects.filter(id=course_id).first()
    assignments = Assignment.objects.filter(course=course)
    return render(request, 'prorector_assignment.html', {'course': course, 'assignments': assignments})

def add_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        course = Course.objects.create(title=title, description=description)

        # Обработка добавления заданий
        assignment_titles = request.POST.getlist('assignment_titles')
        assignment_descriptions = request.POST.getlist('assignment_descriptions')

        for title, description in zip(assignment_titles, assignment_descriptions):
            Assignment.objects.create(course=course, title=title, description=description)

        return redirect('prorector_dashboard')  # Перенаправление на панель проректора

    return render(request, 'add_course.html')

def create_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course = course_form.save()
            return redirect('prorector_dashboard')  # Перенаправление на панель проректора
    else:
        course_form = CourseForm()
    return render(request, 'create_course.html', {'course_form': course_form})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=course)
        if course_form.is_valid():
            course_form.save()
            return redirect('prorector_dashboard')
    else:
        course_form = CourseForm(instance=course)
    assignments = Assignment.objects.filter(course=course)
    return render(request, 'edit_course.html', {'course_form': course_form, 'course': course, 'assignments': assignments})

def add_assignment(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        assignment_form = AssignmentForm(request.POST)
        if assignment_form.is_valid():
            assignment = assignment_form.save(commit=False)
            assignment.course = course
            assignment.save()
            return redirect('edit_course', course_id=course.id)
    else:
        assignment_form = AssignmentForm()
    return render(request, 'add_assignment.html', {'assignment_form': assignment_form, 'course': course})

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    course_id = assignment.course.id
    assignment.delete()
    return redirect('edit_course', course_id=course_id)

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('prorector_dashboard')

def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        assignment_form = AssignmentForm(request.POST, instance=assignment)
        if assignment_form.is_valid():
            assignment_form.save()
            return redirect('prorector_dashboard')
    else:
        assignment_form = AssignmentForm(instance=assignment)
    return render(request, 'edit_assignment.html', {'assignment_form': assignment_form, 'assignment': assignment})

def student_assignment(request, course_id):
    course = Course.objects.filter(id=course_id).first()
    assignments = Assignment.objects.filter(course=course)
    return render(request, 'student_assignment.html', {'course': course, 'assignments': assignments})
