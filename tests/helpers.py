from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import uuid
import urls
import locators

preset_name = 'Viky'
preset_email = '' # should be generated once per session inside create_user_on_backend fixture
preset_password = '' # should be generated once per session inside create_user_on_backend fixture

color_of_selected_ingredients_group = 'rgba(255, 255, 255, 1)'

def generate_email():
    # using randomization of 100-999 per project description. I would prefer to use GUID.
    return f"victoria_kharnovets_9_{random.randint(100, 999)}@mail.com"


def generate_password():
    # generate password from first 16 symbols of generated GUID
    return uuid.uuid4().hex[0:15]

def login(driver):
    driver.get(urls.login_form)

    driver.find_element(By.XPATH, locators.login_form_email_input).send_keys(preset_email)
    driver.find_element(By.XPATH, locators.login_form_password_input).send_keys(preset_password)
    driver.find_element(By.XPATH, locators.login_form_login_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_changes(urls.login_form))