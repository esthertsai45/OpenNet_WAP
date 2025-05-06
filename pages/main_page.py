from pages.common import Base
import time
from locators.locator import Locators


class MainPage(Base):
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://m.twitch.tv/")

    def get_title(self):
        return self.driver.title

