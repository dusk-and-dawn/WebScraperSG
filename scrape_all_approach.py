import time, json, datetime
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_navigation import open_website, setup_driver, scroll_by_pixels
from db import send_to_db

def scrape_data(driver, player_list):
    elements = driver.find_elements(By.CLASS_NAME, 'hLDjoK')
    for element in elements:
        rank = element.find_element(By.CSS_SELECTOR, 'span.Text.gdSPOf').text.rstrip('.')
        name = element.find_element(By.CSS_SELECTOR, 'bdi.Text.ietnEf').text
        country = element.find_element(By.CSS_SELECTOR, 'span.Text.erwlKT').text
        points = element.find_element(By.CSS_SELECTOR, 'span.Text.gYQbnv').text
        if rank == '' or name == '' or country == '' or points == '':
            continue
        else:
            if [rank, name, country, points] not in player_list:
                player_list.append([rank, name, country, points])

def main(url):
    driver = setup_driver()|
    open_website(driver, url)
    player_list = []

    # Perform smooth scrolling and scraping
    end_of_content_reached = False
    while not end_of_content_reached:
        scrape_data(driver, player_list)
        scroll_by_pixels(driver, 700)
        if len(player_list) == 500:
            end_of_content_reached = True
        print(len(player_list))
    driver.quit()
    print(player_list)

    with open('wta500.json', 'w', -1, 'utf-8') as file:
        json.dump(player_list, file)
    
    send_to_db('wtaMasterList', player_list)

main('https://www.sofascore.com/tennis/rankings/wta')



