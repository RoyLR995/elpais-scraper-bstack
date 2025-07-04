import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    chrome_driver_path = r"c:\Users\likhi\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
    service = Service(chrome_driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://elpais.com/")
    yield driver
    driver.quit()

