import logging

from selenium.webdriver.common.keys import Keys

from locators.locator import Locators
from pages.common import Base
from pages.search_result_page import ResultPage


class MainPage(Base):
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        logging.info(f"go to {url} website...")
        self.driver.get(url)
        self.wait_for_element_invisible(*Locators.LOADING)

    def search(self, input_text):
        logging.info(f"search {input_text} ...")
        self.click_element_by_locator(*Locators.BROWSER)
        search_filed = self.find_element(*Locators.SEARCH_FIELD)
        search_filed.clear()
        search_filed.send_keys(input_text)
        search_filed.send_keys(Keys.RETURN)
        return ResultPage(self.driver)
