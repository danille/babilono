from django.shortcuts import render
from .models import Course


# Create your views here.
def main_page(request):
    return render(request, 'main.html')


def courses_page(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'course_list': courses})
