import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from features.pages.BasePg import BasePg


class HomePg(BasePg):
    def __init__(self, driver):
        super().__init__(driver)

    expected_title_text = "Sports News: Live Scores, Results, Schedules of All Sports - myKhel"

    def homepgtitle(self):
        return self.verify_pg_title(self.expected_title_text)

    search_btn_xpath = "//div[@class='oi-header-searchblock']"

    def clickingsrchbtn(self):
        self.clicking("search_btn_xpath", self.search_btn_xpath)
        time.sleep(2)

    search_query_id = "oneindia_search"

    def searching(self, query):
        self.clicking("search_query_id", self.search_query_id)
        time.sleep(2)
        self.type_into_element("search_query_id", self.search_query_id, query)
        time.sleep(2)
        self.press_enter_btn("search_query_id", self.search_query_id)
        time.sleep(5)

    more_btn_xpath = "//a[@class='more']"

    def morebtn_menu(self):
        self.clicking("more_btn_xpath", self.more_btn_xpath)
        time.sleep(2)

    photos_link_xpath = "//a[.=' Photos ']"

    def photos_link(self):
        self.clicking("photos_link_xpath", self.photos_link_xpath)
        time.sleep(2)
