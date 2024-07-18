import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_navigation import scroll_to_bottom, scroll_by_pixels
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
x = driver.get('https://www.sofascore.com/tennis/rankings/wta')
time.sleep(5)

rank_element = driver.find_elements(By.CSS_SELECTOR, 'span.Text.gdSPOf')
names_elements = driver.find_elements(By.CSS_SELECTOR, 'bdi.Text.ietnEf')

# ranks = []
# for rank in rank_element:
#     num = rank.text
#     if num:
#         ranks.append(num)

names = []
for name in names_elements:
    x = name.text
    if x:
        names.append(x)

stop = False
while stop==False:
    ranks = []
    for rank in rank_element:
        num = rank.text
        if num:
            ranks.append(num)
    if ranks[-1] == '500':
        stop = True
    else:
        scroll_by_pixels(driver, 700)
    

print(ranks)
