from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import Locators
from helpers import Helpers

class ElementHasExpectedShadowColor(object):
  def __init__(self, locator, shadow_color):
    self.locator = locator
    self.shadow_color = shadow_color

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.shadow_color in element.value_of_css_property('box-shadow'):
        return element
    else:
        return False

class TestConstructor:

    selected_ingredients_group_shadow_color = '76, 76, 255'

    def test_constructor_page_shown_from_profile_using_profile_button(self, driver):
        Helpers.login(driver)

        driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        driver.find_element(*Locators.profile_page_constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.main_page))
        assert driver.current_url == Urls.main_page

    def test_constructor_page_shown_from_profile_using_logo(self, driver):
        Helpers.login(driver)

        driver.find_element(*Locators.main_page_profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.profile_page))

        driver.find_element(*Locators.profile_page_main_logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.main_page))
        assert driver.current_url == Urls.main_page

    def test_page_is_scrolled_on_fillings(self, driver):
        Helpers.login(driver)

        fillings_label = driver.find_element(*Locators.main_page_fillings_label)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        WebDriverWait(driver, 5).until(ElementHasExpectedShadowColor(Locators.main_page_fillings_control, TestConstructor.selected_ingredients_group_shadow_color))

        shadow = driver.find_element(*Locators.main_page_fillings_control).value_of_css_property('box-shadow')
        assert TestConstructor.selected_ingredients_group_shadow_color in shadow

    def test_page_is_scrolled_on_sauces(self, driver):
        Helpers.login(driver)

        sauces_label = driver.find_element(*Locators.main_page_sauces_label)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_label)

        WebDriverWait(driver, 5).until(ElementHasExpectedShadowColor(Locators.main_page_sauces_control, TestConstructor.selected_ingredients_group_shadow_color))

        shadow = driver.find_element(*Locators.main_page_sauces_control).value_of_css_property('box-shadow')
        assert TestConstructor.selected_ingredients_group_shadow_color in shadow

    def test_page_is_scrolled_on_buns(self, driver):
        Helpers.login(driver)

        fillings_label = driver.find_element(*Locators.main_page_fillings_label)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_label)

        buns_label = driver.find_element(*Locators.main_page_buns_label)
        driver.execute_script("arguments[0].scrollIntoView();", buns_label)

        WebDriverWait(driver, 5).until(ElementHasExpectedShadowColor(Locators.main_page_buns_control, TestConstructor.selected_ingredients_group_shadow_color))

        shadow = driver.find_element(*Locators.main_page_buns_control).value_of_css_property('box-shadow')
        assert TestConstructor.selected_ingredients_group_shadow_color in shadow
