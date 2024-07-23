import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)

def open_website(driver, url):
    driver.get(url)

# Function to scroll by a specific number of pixels
def scroll_by_pixels(driver, pixels):
    driver.execute_script(f"window.scrollBy(0, {pixels});")
    time.sleep(1)  # Adjust the sleep time if necessary
'''
def smooth_scroll(driver, scroll_increment=500, scroll_pause_time=1):
    """Scroll down the webpage incrementally and return True if the end is reached."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_position = 0

    while True:
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(scroll_pause_time)

        # Calculate new scroll position and height
        scroll_position += scroll_increment
        new_height = driver.execute_script("return document.body.scrollHeight")

        if scroll_position >= new_height:
            # Scroll position exceeds or reaches the bottom of the page
            driver.execute_script(f"window.scrollTo(0, {new_height});")
            return True  # End of content reached

        last_height = new_height
'''
