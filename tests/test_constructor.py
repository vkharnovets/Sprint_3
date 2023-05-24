import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators


@pytest.mark.usefixtures("registerUser")
class TestConstructor:
    def test_constructor_page_shown_from_profile_using_profile_button(self, logged_in_driver):
        logged_in_driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(logged_in_driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        logged_in_driver.find_element(*Locators.profile_page_constructor_button).click()
        WebDriverWait(logged_in_driver, 5).until(expected_conditions.url_to_be(Urls.main_page))
        assert logged_in_driver.current_url == Urls.main_page

    def test_constructor_page_shown_from_profile_using_logo(self, logged_in_driver):
        logged_in_driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(logged_in_driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        logged_in_driver.find_element(*Locators.profile_page_main_logo).click()
        WebDriverWait(logged_in_driver, 5).until(expected_conditions.url_to_be(Urls.main_page))
        assert logged_in_driver.current_url == Urls.main_page

    def test_page_is_scrolled_on_fillings(self, logged_in_driver):
        fillings_label = logged_in_driver.find_element(*Locators.main_page_fillings_label)
        logged_in_driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        element = WebDriverWait(logged_in_driver, 5).until(expected_conditions.visibility_of_element_located(Locators.main_page_fillings_control_active))

        assert element is not None

    def test_page_is_scrolled_on_sauces(self, logged_in_driver):
        sauces_label = logged_in_driver.find_element(*Locators.main_page_sauces_label)
        logged_in_driver.execute_script("arguments[0].scrollIntoView();", sauces_label)

        element = WebDriverWait(logged_in_driver, 5).until(expected_conditions.visibility_of_element_located(Locators.main_page_sauces_control_active))

        assert element is not None

    def test_page_is_scrolled_on_buns(self, logged_in_driver):
        fillings_label = logged_in_driver.find_element(*Locators.main_page_fillings_label)
        logged_in_driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        buns_label = logged_in_driver.find_element(*Locators.main_page_buns_label)
        logged_in_driver.execute_script("arguments[0].scrollIntoView();", buns_label)

        element = WebDriverWait(logged_in_driver, 5).until(expected_conditions.visibility_of_element_located(Locators.main_page_buns_control_active))

        assert element is not None
