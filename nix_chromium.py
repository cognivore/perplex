from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from nix_utils import nix_which

def mk_webdriver():
    options = Options()
    options.binary_location = nix_which("chromium")  # Izmanto musu funkciju, lai atrastu Chromium atrašanās vietu
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path=nix_which("chromedriver"))  # Izmanto funkciju arī šeit

    driver = webdriver.Chrome(service=service, options=options)
    return driver
