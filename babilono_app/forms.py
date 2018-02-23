from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, StudentLecture, StudentCourse, Teacher


class StudentSignUpForm(UserCreationForm):
    phone_number = forms.RegexField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': '+48999999999'}),
                                    regex=r'^(\+48)?\d{9,12}$')
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Miejscowość'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Login'
                                                      }),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Hasło'
                                                           }),
                   'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Wprowadź swoje hasło ponownie'
                                                           }),
                   'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Imie', }),
                   'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Nazwisko'})
                   }

    def save(self, commit=True):
        user = super().save(commit=True)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.city = self.city
        student.phone_number = self.phone_number
        student.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    phone_number = forms.RegexField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': '+48999999999'}),
                                    regex=r'^(\+48)?\d{9,12}$')
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Miejscowość'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Instytucja'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Login'
                                                      }),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Hasło'
                                                           }),
                   'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Wprowadź swoje hasło ponownie'
                                                           }),
                   'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Imie', }),
                   'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Nazwisko'})
                   }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.institution = self.institution
        teacher.city = self.city
        teacher.phone_number = self.phone_number
        teacher.save()
        return user


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",
                                                             'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Hasło'}))


class StudentLectureForm(forms.ModelForm):
    class Meta:
        model = StudentLecture
        fields = ('lecture', 'rating', )
        widgets = {'rating': forms.Select(choices=[(1, '1'),
                                                   (2, '2'),
                                                   (3, '3'),
                                                   (4, '4'),
                                                   (5, '5')],
                                          attrs={'class': 'form-control'}),
                   'lecture': forms.TextInput(attrs={'readonly': True})
                   }
