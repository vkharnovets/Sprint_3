from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators
from helpers import Helpers


class TestRegistration:
    def test_successful_registration(self, driver):
        Helpers.register(driver)
        assert driver.current_url == Urls.login_form

    def test_failed_registration_wrong_password(self, driver):
        driver.get(Urls.register_form)

        driver.find_element(*Locators.reg_form_name_input).send_keys('Viky')
        driver.find_element(*Locators.reg_form_email_input).send_keys(Helpers.generate_email())
        driver.find_element(*Locators.reg_form_password_input).send_keys('12345')
        driver.find_element(*Locators.reg_form_confirm_button).click()

        # ensure "incorrect password" label is created
        assert len(driver.find_elements(*Locators.reg_form_wrong_password_label)) == 1
