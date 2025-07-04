from dotenv import load_dotenv
import os
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
BASE_URL = os.getenv("BASE_URL", "https://elpais.com/")

BSTACK_USERNAME = os.getenv("BSTACK_USER_NAME")
BSTACK_ACCESS_KEY = os.getenv("BSTACK_ACCESS_KEY")


BROWSERSTACK_CONFIGS=[
    #Windows Edge
    {
        "browser": "Edge",
        "browser_version": "137.0",
        "os": "Windows",
        "os_version": "11",
        "build": "Parallel Build"
    },
    #Windows Firefox
    {
        "browser": "Firefox",
        "browser_version": "138",
        "os": "Windows",
        "os_version": "10",
        "build": "Parallel Build"
    },
    #OS X Firefox
    {
        "browser": "Firefox",
        "browser_version": "latest",
        "os": "OS X",
        "os_version": "Sonoma",
        "build": "Parallel Build"
    },
    #OS X Edge
    {
        "browser": "Edge",
        "browser_version": "latest",
        "os": "OS X",
        "os_version": "Monterey",
        "build": "Parallel Build"
    },
    #OS X Firefox
    {
        "browser": "Firefox",
        "browser_version": "139.0",
        "os": "OS X",
        "os_version": "Ventura",
        "build": "Parallel Build"
    },
]


