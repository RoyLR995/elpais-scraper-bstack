import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.title_store import TitleStore

class OpinionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    ARTICLE_BLOCKS = (By.CSS_SELECTOR, "article")

    def get_first_5_articles(self):
        self.wait.until(EC.presence_of_all_elements_located(self.ARTICLE_BLOCKS))
        return self.driver.find_elements(*self.ARTICLE_BLOCKS)[:5]

    def open_article_in_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def extract_article_data(self, article_element, index):
        try:
            link = article_element.find_element(By.CSS_SELECTOR, "h2 a")
            article_url = link.get_attribute("href")
        except:
            print(f"Article {index}: No valid link found.")
            return

        original_tab = self.driver.current_window_handle
        self.open_article_in_new_tab(article_url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "article")))

        # Extract Title
        try:
            title = self.driver.find_element(By.TAG_NAME, "h1").text
        except:
            title = "No title found"

        TitleStore.add_title(title)

        # Extract Content
        try:
            content = self.driver.find_element(By.TAG_NAME, "h2").text
        except:
            content = "No content found"

        # Extract image
        image_url = ""
        try:
            image = self.driver.find_element(By.CSS_SELECTOR, "article img")
            image_url = image.get_attribute("src")
            self.download_image(image_url, f"article_{index}.jpg")
        except:
            print(f"Article {index}: No image found.")

        print(f"\n Article {index}")
        print(f"Title   : {title}")
        print(f"Content : {content}")
        if image_url:
            print(f"Image   : Downloaded.")

        self.driver.close()
        self.driver.switch_to.window(original_tab)

    def download_image(self, url, filename):
        try:
            os.makedirs("downloads", exist_ok=True)
            img_data = requests.get(url, timeout=10).content
            with open(os.path.join("downloads", filename), "wb") as f:
                f.write(img_data)
        except Exception as e:
            print(f"Failed to download image: {e}")
