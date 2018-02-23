"""babilono URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin

from babilono_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('courses/', views.courses_page, name='courses'),
    path('courses/<int:pk>/', views.enroll_in_course, name='enroll-in-course'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/students/signup', views.student_signup, name='student-signup'),
    path('accounts/teachers/signup', views.teacher_signup, name='teacher-signup'),
    path('accounts/students/courses', views.student_course_list, name='student-course-list'),
    path('signin/', views.sign_in, name='sign-in'),
]
