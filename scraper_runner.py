from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import BASE_URL, BSTACK_USERNAME, BSTACK_ACCESS_KEY, CHROME_DRIVER_PATH
from tests.test_lang_check import test_language_label_is_spanish
from tests.test_opinion import test_scrape_opinion_articles
from tests.test_translation import test_translate_titles_and_count

def run_scraper(remote=False, capabilities=None):
    if remote:
        options = webdriver.ChromeOptions()
        for key, value in capabilities.items():
            options.set_capability(key, value)

        url = f"http://{BSTACK_USERNAME}:{BSTACK_ACCESS_KEY}@hub.browserstack.com/wd/hub"
        driver = webdriver.Remote(command_executor=url, options=options)

        print(f" Running remotely on BrowserStack: {capabilities.get('browser')} {capabilities.get('os')}")
    else:
        chrome_driver_path = CHROME_DRIVER_PATH
        service = Service(chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        print(" Running locally")

    try:
        driver.get(BASE_URL)
        test_language_label_is_spanish(driver)
        test_scrape_opinion_articles(driver)
        test_translate_titles_and_count()
    finally:
        driver.quit()
