import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Device:
    iPhoneX = "iPhone X"
    GalaxyS5 = "Galaxy S5"

def get_driver(device_name):
    mobile_emulation = { "deviceName": device_name }
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture
def driver():
    driver = get_driver(Device.GalaxyS5)
    yield driver
    driver.quit()
