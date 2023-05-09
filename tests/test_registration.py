from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators
from helpers import Helpers


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Urls.register_form)

        driver.find_element(By.XPATH, Locators.reg_form_name_input).send_keys(Helpers.preset_name)
        driver.find_element(By.XPATH, Locators.reg_form_email_input).send_keys(Helpers.generate_email())
        driver.find_element(By.XPATH, Locators.reg_form_password_input).send_keys(Helpers.generate_password())
        driver.find_element(By.XPATH, Locators.reg_form_confirm_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.register_form))
        assert driver.current_url == Urls.login_form

    def test_failed_registration_wrong_password(self, driver):
        driver.get(Urls.register_form)

        # ensure "incorrect password" label does not exist at start
        assert len(driver.find_elements(By.XPATH, Locators.reg_form_wrong_password_label)) == 0

        driver.find_element(By.XPATH, Locators.reg_form_name_input).send_keys('Viky')
        driver.find_element(By.XPATH, Locators.reg_form_email_input).send_keys(Helpers.generate_email())
        driver.find_element(By.XPATH, Locators.reg_form_password_input).send_keys('12345')
        driver.find_element(By.XPATH, Locators.reg_form_confirm_button).click()

        # ensure "incorrect password" label is now created
        assert len(driver.find_elements(By.XPATH, Locators.reg_form_wrong_password_label)) == 1
