from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import urls
import locators
import helpers

class TestConstructor:

    def test_constructor_page_shown_from_profile_using_profile_button(self, driver):
        helpers.login(driver)

        driver.find_element(By.XPATH, locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(urls.profile_page))

        driver.find_element(By.XPATH, locators.profile_page_constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(urls.main_page))
        assert driver.current_url == urls.main_page

    def test_constructor_page_shown_from_profile_using_logo(self, driver):
        helpers.login(driver)

        driver.find_element(By.XPATH, locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(urls.profile_page))

        driver.find_element(By.XPATH, locators.profile_page_main_logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(urls.main_page))
        assert driver.current_url == urls.main_page

    def test_page_is_scrolled_on_fillings(self, driver):
        helpers.login(driver)

        fillings_label = driver.find_element(By.XPATH, locators.main_page_fillings_label)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        time.sleep(1)

        color = driver.find_element(By.XPATH, locators.main_page_fillings_control).value_of_css_property('color')
        assert color == helpers.color_of_selected_ingredients_group


    def test_page_is_scrolled_on_sauces(self, driver):
        helpers.login(driver)

        sauces_label = driver.find_element(By.XPATH, locators.main_page_sauces_label)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_label)

        time.sleep(1)

        color = driver.find_element(By.XPATH, locators.main_page_sauces_control).value_of_css_property('color')
        assert color == helpers.color_of_selected_ingredients_group

    def test_page_is_scrolled_on_buns(self, driver):
        helpers.login(driver)

        fillings_label = driver.find_element(By.XPATH, locators.main_page_fillings_label)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        time.sleep(1)
        color = driver.find_element(By.XPATH, locators.main_page_buns_control).value_of_css_property('color')
        assert color != helpers.color_of_selected_ingredients_group

        buns_label = driver.find_element(By.XPATH, locators.main_page_buns_label)
        driver.execute_script("arguments[0].scrollIntoView();", buns_label)

        time.sleep(1)
        color = driver.find_element(By.XPATH, locators.main_page_buns_control).value_of_css_property('color')
        assert color == helpers.color_of_selected_ingredients_group
