from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Course, Lecture, StudentCourse, StudentLecture
from .forms import StudentSignUpForm, TeacherSignUpForm, SignInForm, StudentLectureForm


# Create your views here.
def home_page(request):
    return render(request, 'main.html')


def courses_page(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'course_list': courses})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            print('sign-up form is valid. redirecting...')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = StudentSignUpForm()
    return render(request, 'student_signup.html', {'form': form})


def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = TeacherSignUpForm()

    return render(request, 'teacher_signup.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            print('sign-in form is valid. redirecting...')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})


# @student_required
def enroll_in_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    student = request.user.student

    if student.courses.filter(pk=pk).exists():
        return render(request, 'taken_courses.html')

    StudentCourse.objects.create(student=student, course=course)
    for lecture in course.lecture_set.all():
        StudentLecture.objects.create(student=student, lecture=lecture)

    return redirect('student-course-list')


# @student_required
def student_course_list(request):
    student = request.user.student
    student_lectures = student.lectures.all()
    student_courses = student.courses.all()

    if request.method == 'POST':
        form = StudentLectureForm(request.POST)
        form.save()
    else:
        form = StudentLectureForm()

    return render(request, 'taken_courses.html', {'courses': student_courses,
                                                  'lectures': student_lectures,
                                                  'form': form})
