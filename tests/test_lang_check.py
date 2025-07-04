import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from pages.home_page import HomePage

def test_language_label_is_spanish(driver):
    home = HomePage(driver)
    home.accept_cookies_if_present()
    label = home.get_espana_label_text()
    assert label.upper() == "ESPAÑA"
    print("Language is Spanish")
