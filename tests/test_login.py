from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators
from helpers import Helpers


class TestLogin:
    def test_login_page_shown_by_login_button(self, driver):
        driver.get(Urls.main_page)
        driver.find_element(By.XPATH, Locators.main_page_login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.main_page))
        assert driver.current_url == Urls.login_form

    def test_login_page_shown_by_profile_button(self, driver):
        driver.get(Urls.main_page)
        driver.find_element(By.XPATH, Locators.main_page_profile_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.main_page))
        assert driver.current_url == Urls.login_form

    def test_login_page_shown_by_login_link_from_register_form(self, driver):
        driver.get(Urls.register_form)
        driver.find_element(By.XPATH, Locators.reg_form_login_link).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.main_page))
        assert driver.current_url == Urls.login_form

    def test_login_page_shown_by_login_link_from_forgot_password_page(self, driver):
        driver.get(Urls.forgot_password_page)
        driver.find_element(By.XPATH, Locators.forgot_password_page_login_link).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.main_page))
        assert driver.current_url == Urls.login_form

    def test_successful_login(self, driver):
        Helpers.login(driver)
        assert driver.current_url == Urls.main_page

        # ensure "create order" button is shown on the page
        assert len(driver.find_elements(By.XPATH, Locators.main_page_create_order_button)) == 1
