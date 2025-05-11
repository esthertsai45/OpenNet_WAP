from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(device_name):
    mobile_emulation = { "deviceName": device_name }
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    return driver
