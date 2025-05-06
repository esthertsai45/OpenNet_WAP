from selenium.webdriver.common.by import By


class Locators:
    MAIN_TITLE = (By.ID, "Twitch")
    SEARCH = (By.XPATH, "//div[text()='Browse'")
    SEARCH_FIELD = (By.XPATH, "data-a-target='tw-input'")
 