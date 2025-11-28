import time


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser

from main_app.tests.test_coopesma_base import CoopesmaMixin


class CoopesmaBaseFunctionalTest(StaticLiveServerTestCase, CoopesmaMixin):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)
