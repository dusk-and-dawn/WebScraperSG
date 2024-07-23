import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_navigation import open_website, scroll_by_pixels


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://www.sofascore.com/tennis/rankings/wta')

while True:
    try:
        x = 0
        elements = driver.find_elements(By.CLASS_NAME, 'hLDjoK')
        player_list = []
        for element in elements:
            rank = element.find_element(By.CSS_SELECTOR, 'span.Text.gdSPOf').text.rstrip('.')
            name = element.find_element(By.CSS_SELECTOR, 'bdi.Text.ietnEf').text
            country = element.find_element(By.CSS_SELECTOR, 'span.Text.erwlKT').text
            points = element.find_element(By.CSS_SELECTOR, 'span.Text.gYQbnv').text
            if rank == '' or name == '' or country == '' or points == '':
                driver.execute_script(f"window.scrollBy(0, {500});")
                time.sleep(1)  # Adjust the sleep time if necessary
                x += 1
                if x == 20:
                    break
            else:
                player_list.append([rank, name, country, points])
                x += 1
                if x == 20:
                    break
    except:
        pass

print(player_list)

