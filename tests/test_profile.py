from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators
from helpers import Helpers


class TestProfile:
    def test_profile_page_shown_by_profile_button(self, driver):
        Helpers.login(driver)

        driver.find_element(By.XPATH, Locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))
        assert driver.current_url == Urls.profile_page

    def test_logout_by_profile_logout_button(self, driver):
        Helpers.login(driver)

        driver.find_element(By.XPATH, Locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        driver.find_element(By.XPATH, Locators.profile_page_logout_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.login_form))
        assert driver.current_url == Urls.login_form
