import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Setup Chrome service with ChromeDriverManager to automatically handle the driver for the current version of Chrome
    s = Service(ChromeDriverManager().install())
    # Initialize the Chrome WebDriver with the service
    driver = webdriver.Chrome(service=s)

    yield driver
    driver.quit()
