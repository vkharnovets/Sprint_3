from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from urls import Urls
from locators import Locators


class Helpers:
    preset_name = 'Viky'
    preset_email = ''  # should be generated once per session inside create_user_on_backend fixture
    preset_password = ''  # should be generated once per session inside create_user_on_backend fixture

    color_of_selected_ingredients_group = 'rgba(255, 255, 255, 1)'

    @staticmethod
    def generate_email():
        fake = Faker()
        fake.name()

        return f"victoria_kharnovets_9_{fake.random_number(digits=3)}@{fake.domain_name()}"

    @staticmethod
    def generate_password():
        fake = Faker()
        fake.name()

        return fake.password(length=14, special_chars=True, digits=True, upper_case=True, lower_case=True)

    @staticmethod
    def login(driver):
        driver.get(Urls.login_form)

        driver.find_element(By.XPATH, Locators.login_form_email_input).send_keys(Helpers.preset_email)
        driver.find_element(By.XPATH, Locators.login_form_password_input).send_keys(Helpers.preset_password)
        driver.find_element(By.XPATH, Locators.login_form_login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.login_form))
