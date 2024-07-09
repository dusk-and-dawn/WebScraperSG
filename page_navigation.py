# page navigation

import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Scroll to the bottom of the page to ensure all elements are loaded
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        # Function to scroll by a specific number of pixels
def scroll_by_pixels(driver, pixels):
    driver.execute_script(f"window.scrollBy(0, {pixels});")
    time.sleep(1)  # Adjust the sleep time if necessary

# Scroll in increments of 500 pixels until the bottom of the page
    last_height = driver.execute_script("return document.body.scrollHeight")
    pixels_to_scroll = 500
