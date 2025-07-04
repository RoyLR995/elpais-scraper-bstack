from dotenv import load_dotenv
import os
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
BASE_URL = BASE_URL = os.getenv("BASE_URL", "https://elpais.com/")
