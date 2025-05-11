from pages.main_page import MainPage

import time


def test_search_and_watch_video(driver):
    page = MainPage(driver)
    page.load("https://m.twitch.tv/")
    result_page = page.search("StarCraft II")
    for _ in range(2):
        time.sleep(1)
        result_page.scroll_to_position(0, 100)
    result_page.click_video()
