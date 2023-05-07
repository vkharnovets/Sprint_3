import pytest
from selenium import webdriver
import requests
import helpers
import urls


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def create_user_on_backend():
    helpers.preset_email = helpers.generate_email()
    helpers.preset_password = helpers.generate_password()

    payload = {
        "name": "Viky",
        "email": helpers.preset_email,
        "password": helpers.preset_password
    }
    response = requests.post(url=urls.register_api, json=payload)
    assert response.status_code == 200
