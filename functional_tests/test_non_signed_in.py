from .base import FunctionalTest


class NonLoggedInTest(FunctionalTest):
    def test_user_can_browse_main_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn("Babilono", self.browser.title)

    def test_user_can_browse_course_list(self):
        self.browser.get(self.live_server_url + '/courses/')
        self.assertIn('Courses', self.browser.title)
        # Add here verification of course table existence


