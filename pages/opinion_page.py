import os
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.title_store import TitleStore

class OpinionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_first_5_articles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "article")[:3]

    def extract_article_data(self, article_element, index):
        try:
            link_element = article_element.find_element(By.CSS_SELECTOR, "h2 a")
            article_url = link_element.get_attribute("href")
        except Exception as e:
            print(f"Article {index}: No valid link found.")
            return

        original_tab = self.driver.current_window_handle

        # Open in new tab
        self.driver.execute_script("window.open(arguments[0], '_blank');", article_url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))

        # Extract full title
        try:
            title = self.driver.find_element(By.TAG_NAME, "h1").text
        except:
            title = "No title found"

        # Extract content
        try:
            content = self.driver.find_element(By.TAG_NAME, "h2").text
        except:
            content = "No content found"

        # Extract image
        image_url = ""
        try:
            img_element = self.driver.find_element(By.CSS_SELECTOR, "article img")
            image_url = img_element.get_attribute("src") or img_element.get_attribute("data-src")
            if image_url:
                self.download_image(image_url, f"article_{index}.jpg")
        except:
            print(f"No image found for Article {index}")

        TitleStore.add_title(title)

        print(f"\nArticle {index}")
        print(f"Title   : {title}")
        print(f"Content : {content}")
        if image_url:
            print(f"Image   : Downloaded.")

        self.driver.close()
        time.sleep(3)
        self.driver.switch_to.window(original_tab)


    def download_image(self, url, filename):
        try:
            os.makedirs("downloads", exist_ok=True)
            img_data = requests.get(url, timeout=10).content
            with open(os.path.join("downloads", filename), "wb") as f:
                f.write(img_data)
        except Exception as e:
            print(f"Failed to download image: {e}")
