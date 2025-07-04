# pages/home_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    COOKIE_ACCEPT_BTN = (By.ID, "didomi-notice-agree-button")
    ESPANA_LABEL = (By.CSS_SELECTOR, "li[data-edition='el-pais'] span")
    OPINION_LINK = (By.LINK_TEXT, "Opinión")

    # Actions
    def accept_cookies_if_present(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BTN))
            btn.click()
            print("Cookies accepted.")
        except:
            print("Cookie popup not shown.")

    def get_espana_label_text(self):
        label = self.wait.until(EC.visibility_of_element_located(self.ESPANA_LABEL))
        return label.text.strip()

    def go_to_opinion_section(self):
        link = self.wait.until(EC.element_to_be_clickable(self.OPINION_LINK))
        link.click()
        print("Navigated to Opinión section.")
