import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
#driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://www.sofascore.com/tennis/rankings/wta')

time.sleep(3)

players = driver.find_elements(By.CSS_SELECTOR, '#__next > main > div > div > div.Box.clAhaB.Col.bzYVms > div > div.Box.cORqut > div:nth-child(4) > div > a > div > div.Box.Flex.eEidkY.hURKmT > bdi')
# player_names = [player.text for player in players]
lst_players = []
for i in range(3,104):
    string = '#__next > main > div > div > div.Box.clAhaB.Col.bzYVms > div > div.Box.cORqut > div:nth-child(' + str(i) + ') > div > a > div > div.Box.Flex.eEidkY.hURKmT > bdi'
    temp = driver.find_elements(By.CSS_SELECTOR, string)
    temp2 = [j.text for j in temp]
    lst_players.append(temp2)
driver.quit()
print(f'player names: {lst_players}')
print(f'player names: {players}')

