from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators
from test_login import TestLogin

class TestConstructor:

    selected_ingredients_group_shadow_color = '76, 76, 255'

    def test_constructor_page_shown_from_profile_using_profile_button(self, driver):
        TestLogin.test_successful_login(driver)

        driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        driver.find_element(*Locators.profile_page_constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.main_page))
        assert driver.current_url == Urls.main_page

    def test_constructor_page_shown_from_profile_using_logo(self, driver):
        TestLogin.test_successful_login(driver)

        driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        driver.find_element(*Locators.profile_page_main_logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.main_page))
        assert driver.current_url == Urls.main_page

    def test_page_is_scrolled_on_fillings(self, driver):
        TestLogin.test_successful_login(driver)

        fillings_label = driver.find_element(*Locators.main_page_fillings_label)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.main_page_fillings_control_active))

        assert element is not None

    def test_page_is_scrolled_on_sauces(self, driver):
        TestLogin.test_successful_login(driver)

        sauces_label = driver.find_element(*Locators.main_page_sauces_label)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_label)

        element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.main_page_sauces_control_active))

        assert element is not None

    def test_page_is_scrolled_on_buns(self, driver):
        TestLogin.test_successful_login(driver)

        fillings_label = driver.find_element(*Locators.main_page_fillings_label)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        buns_label = driver.find_element(*Locators.main_page_buns_label)
        driver.execute_script("arguments[0].scrollIntoView();", buns_label)

        element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.main_page_buns_control_active))

        assert element is not None
