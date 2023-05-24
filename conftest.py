import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators
from helpers import Helpers


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def logged_in_driver(driver):
    driver.get(Urls.login_form)

    driver.find_element(*Locators.login_form_email_input).send_keys(Helpers.preset_email)
    driver.find_element(*Locators.login_form_password_input).send_keys(Helpers.preset_password)
    driver.find_element(*Locators.login_form_login_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.login_form))

    yield driver


@pytest.fixture(scope="session")
def registerUser():
    driver = webdriver.Chrome()
    driver.get(Urls.register_form)

    Helpers.preset_email = Helpers.generate_email()
    Helpers.preset_password = Helpers.generate_password()

    driver.find_element(*Locators.reg_form_name_input).send_keys(Helpers.preset_name)
    driver.find_element(*Locators.reg_form_email_input).send_keys(Helpers.preset_email)
    driver.find_element(*Locators.reg_form_password_input).send_keys(Helpers.preset_password)
    driver.find_element(*Locators.reg_form_confirm_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_changes(Urls.register_form))

    driver.quit()
