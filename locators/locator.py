from selenium.webdriver.common.by import By


class Locators:
    ALL_CONTENT = (By.ID, "page-main-content-wrapper")
    LOADING = (By.XPATH, "//*[contains(@class, 'ScLoadingSpinnerCircle')]")
    BROWSER = (
        By.XPATH, "//div[text()='瀏覽' and contains(@class, 'CoreText-sc-1txzju1-0')]")
    SEARCH_FIELD = (By.XPATH, "//input[@data-a-target='tw-input']")

    # search page locators
    SEARCH_RESULT_TAB = (By.XPATH, "//ul[@role='tablist']")
    VIDEO_IMAGE = (By.XPATH, "//*[@class='tw-image']")
    VIDEO_LINK = (
        By.XPATH, '//a[contains(@class, "tw-link") and starts-with(@href, "/video")]')

    # player locators
    PLAYER = (By.XPATH, '//video[@playsinline and @webkit-playsinline]')
    PLAYER_ALERT = (
        By.XPATH, '//*[@data-test-selector="muted-segments-alert-overlay-presentation__scroll-wrapper"]')
    PLAYER_ALERT_CLOSE = (
        By.XPATH, '//*[@data-test-selector="muted-segments-alert-overlay-presentation__dismiss-button"]')
