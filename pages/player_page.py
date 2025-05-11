from locators.locator import Locators
from pages.common import Base


class PlayerPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_visible(*Locators.PLAYER)
        if self.find_element(*Locators.PLAYER_ALERT):
            self.click_element_by_locator(*Locators.PLAYER_ALERT_CLOSE)
        self.wait_for_element_invisible(*Locators.LOADING, timeout=30)
