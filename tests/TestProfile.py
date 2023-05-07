from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
import locators
import helpers

class TestProfile:
    def test_profile_page_shown_by_profile_button(self, driver):
        helpers.login(driver)

        driver.find_element(By.XPATH, locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(urls.profile_page))
        assert driver.current_url == urls.profile_page

    def test_logout_by_profile_logout_button(self, driver):
        helpers.login(driver)

        driver.find_element(By.XPATH, locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(urls.profile_page))

        driver.find_element(By.XPATH, locators.profile_page_logout_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(urls.login_form))
        assert driver.current_url == urls.login_form

