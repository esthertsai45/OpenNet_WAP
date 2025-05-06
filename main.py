from pages.main_page import MainPage

def test_search(driver):
    page = MainPage(driver)
    page.load()
