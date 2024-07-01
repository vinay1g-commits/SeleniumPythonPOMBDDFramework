from features.pages.BasePg import BasePg


class PhotosPg(BasePg):
    def __init__(self, driver):
        super().__init__(driver)

    Latest_photo_title_xpath = "//span[.='Latest Photos']"

    def photos_pg_assertion(self):
        assert self.element_displayed("Latest_photo_title_xpath", self.Latest_photo_title_xpath)
