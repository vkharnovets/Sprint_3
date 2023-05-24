import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators


@pytest.mark.usefixtures("registerUser")
class TestProfile:
    def test_profile_page_shown_by_profile_button(self, logged_in_driver):
        logged_in_driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(logged_in_driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        assert logged_in_driver.current_url == Urls.profile_page

    def test_logout_by_profile_logout_button(self, logged_in_driver):
        logged_in_driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(logged_in_driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        logged_in_driver.find_element(*Locators.profile_page_logout_button).click()
        WebDriverWait(logged_in_driver, 5).until(expected_conditions.url_to_be(Urls.login_form))

        assert logged_in_driver.current_url == Urls.login_form
