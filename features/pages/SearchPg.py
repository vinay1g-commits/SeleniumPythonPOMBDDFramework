from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.BasePg import BasePg


class SearchPg(BasePg):
    def __init__(self, driver):
        super().__init__(driver)

    google_text_xpath = "//span[@class='gcsc-find-more-on-google-text']"

    def searchpgassertion(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.google_text_xpath))
        )
        assert self.element_displayed("google_text_xpath", self.google_text_xpath)
        # Optional: add additional assertion to check for visibility
        assert self.driver.find_element(By.XPATH, self.google_text_xpath).is_displayed()
