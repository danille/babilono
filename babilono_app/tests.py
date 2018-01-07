from django.test import TestCase


# Create your tests here.
class MainPageTest(TestCase):
    def test_uses_main_page_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'main.html')


class CourseListTest(TestCase):
    def test_uses_courses_template(self):
        response = self.client.get('/courses/')
        self.assertTemplateUsed(response, 'courses.html')
