import pytest

from framework.locators.click_inputs import click_inputsLocators
from framework.web_elements import WebPage


@pytest.mark.usefixtures("setup")
class Testsclickinputs:

    def test_click_inputs(self):
        browser = WebPage(self.driver)

        browser.page_is_opened(click_inputsLocators.LINK)

        assert browser.element_is_present(*click_inputsLocators.Element_inputs) and browser.element_is_clickable(*click_inputsLocators.Element_inputs)