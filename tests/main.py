from pages.main_page import MainPage


def test_search_and_watch_video(driver):
    page = MainPage(driver)
    page.load("https://m.twitch.tv/")
    search_result = page.search("StarCraft II")
    search_result.scroll_to_bottom()
    player = search_result.click_video()
    player.take_screenshot("/screenshots/video.png")
