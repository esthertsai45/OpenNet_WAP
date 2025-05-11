import pytest
from drivers.chrome_driver import get_driver


class Device:
    iPhoneX = "iPhone X"
    GalaxyS5 = "Galaxy S5"


@pytest.fixture
def driver():
    driver = get_driver(Device.GalaxyS5)
    yield driver
    driver.quit()
