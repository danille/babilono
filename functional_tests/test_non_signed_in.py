from .base import FunctionalTest
from babilono_app.models import Course
import time


class NonLoggedInTest(FunctionalTest):
    def test_user_can_browse_main_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn("Babilono", self.browser.title)

    def test_user_can_browse_course_list(self):
        # At first, create two courses. English and German
        english = Course(title="English")
        english.save()

        german = Course(title="German")
        german.save()

        self.browser.get(self.live_server_url + '/courses/')
        self.assertIn('Courses', self.browser.title)
        # Add here verification of course list existence
        course_list_text = self.browser.find_element_by_id('course-list').text
        self.wait_for(lambda: self.assertIn("ENGLISH", course_list_text))
        self.wait_for(lambda: self.assertIn("GERMAN", course_list_text))
