from pages.common import Base
from pages.player_page import PlayerPage
from locators.locator import Locators


class ResultPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_invisible(*Locators.LOADING)
        self.wait_for_element_visible(*Locators.SEARCH_RESULT_TAB)
        self.wait_for_element_visible(*Locators.VIDEO_IMAGE)

    def click_video(self):
        videos = self.find_elements(*Locators.VIDEO_LINK)
        self.click_element_by_element(videos[0])
        return PlayerPage(self.driver)
