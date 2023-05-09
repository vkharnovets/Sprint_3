import pytest
from selenium import webdriver
import requests
from helpers import Helpers
from urls import Urls


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def create_user_on_backend():
    Helpers.preset_email = Helpers.generate_email()
    Helpers.preset_password = Helpers.generate_password()

    payload = {
        "name": "Viky",
        "email": Helpers.preset_email,
        "password": Helpers.preset_password
    }
    response = requests.post(url=Urls.register_api, json=payload)
    assert response.status_code == 200
