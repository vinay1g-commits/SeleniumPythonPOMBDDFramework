from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePg:
    def __init__(self, driver):
        self.driver = driver

    def verify_pg_title(self, expected_title):
        return self.driver.title == expected_title

    def get_element(self, locator_type, locator_value):
        if locator_type.endswith("_id"):
            return self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_xpath"):
            return self.driver.find_element(By.XPATH, locator_value)

    def clicking(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()

    def type_into_element(self, locator_type, locator_value, text_to_enter):
        element = self.get_element(locator_type, locator_value)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element)).clear()
        element.send_keys(text_to_enter)

    def press_enter_btn(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.send_keys(Keys.ENTER)

    def element_displayed(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()
