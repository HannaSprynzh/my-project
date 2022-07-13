import pytest
import time
from framework.web_elements import WebPage
from framework.locators.scroll import Scroll

@pytest.mark.usefixtures("setup")
class Testscroll:
    def test_scroll(self):

        browser = WebPage(self.driver)

        browser.page_is_opened(Scroll.LINK)
        time.sleep(5)
        browser.scroll_to(0, 2000)
        time.sleep(10)


