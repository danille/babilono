from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Course
from .forms import SignUpForm, SignInForm


# Create your views here.
def main_page(request):
    return render(request, 'main.html')


def courses_page(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'course_list': courses})


def pupil_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.pupil.name = form.cleaned_data.get('first_name')
            user.pupil.surname = form.cleaned_data.get('last_name')
            user.pupil.email = form.cleaned_data.get('email')
            user.pupil.city = form.cleaned_data.get('city')
            user.pupil.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            print('sign-up form is valid. redirecting...')
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def teacher_signup(request):
    pass


def sign_in(request):
    if request.method == 'post':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            print('sign-in form is valid. redirecting...')
            return redirect('main')
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})