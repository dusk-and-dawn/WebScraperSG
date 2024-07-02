import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
#driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://www.sofascore.com/tennis/rankings/wta')

time.sleep(5)

players = driver.find_elements(By.CSS_SELECTOR, '#__next > main > div > div > div.Box.clAhaB.Col.bzYVms > div')
player_names = [player.text for player in players]

driver.quit()
print(f'player names: {player_names}')
