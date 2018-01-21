from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField(max_length=35)
    surname = models.TextField(max_length=45)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    city = models.TextField()
    institution = models.TextField(default='')


class Course(models.Model):
    title = models.CharField(default='', max_length=240)
    description = models.TextField(default='')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)


class Difficulty(models.Model):
    level = models.CharField(max_length=120, default='Beginner')


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=240)
    level = models.ForeignKey(Difficulty, on_delete=models.SET_NULL, null=True)
    content = models.FileField(upload_to=f'lectures/', name='')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=35)
    surname = models.TextField(max_length=45)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    city = models.TextField()
    institution = models.TextField(default='', blank=True)
    courses = models.ManyToManyField(Course, through='StudentCourse')
    lectures = models.ManyToManyField(Lecture, through='StudentLecture')


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class StudentLecture(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_lectures')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
