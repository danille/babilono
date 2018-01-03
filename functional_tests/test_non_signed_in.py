from .base import FunctionalTest


class MainPageTest(FunctionalTest):
    def test_user_can_browse_main_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn("Babilono", self.browser.title)

