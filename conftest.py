import pytest
from drivers.chrome_driver import get_driver

@pytest.fixture
def driver():
    driver = get_driver("iPhone X")
    yield driver
    driver.quit()