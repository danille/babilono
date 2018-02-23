from django.contrib import admin
from .models import Lecture, Course, Teacher, StudentLecture


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(StudentLecture)
