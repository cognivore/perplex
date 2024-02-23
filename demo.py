#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import logging
import hashlib
import csv
import sys
import os

# We don't want to hard-code the path to the chromedriver, so we use a helper function to get it
from nix_utils import nix_which

options = Options()
options.binary_location = nix_which("chromium")
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
options.add_argument('--no-sandbox')  # /!\ Bypass OS security model
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

service = Service(executable_path=nix_which("chromedriver"))

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://zerohr.io")

soup = bs(driver.page_source, 'html.parser')

print(soup.get_text())
