import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
#driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://www.sofascore.com/tennis/rankings/wta')

# time.sleep(3)

# players = driver.find_elements(By.CSS_SELECTOR, '#__next > main > div > div > div.Box.clAhaB.Col.bzYVms > div > div.Box.cORqut')
# player_names = [player.text for player in players]
# lst_players = []
# driver.quit()
# print(f'player names: {player_names}')
# print(f'session name: {players}')
lst=[]
# Define a function to scroll to the bottom of the page

elements = driver.find_elements(By.CSS_SELECTOR, '#__next > main > div > div > div.Box.clAhaB.Col.bzYVms > div > div.Box.cORqut')
for element in elements:
    lst.append(element.text)

# Close the driver
driver.quit()

# Cleaning operations 
#print(lst)
clean = str(lst).replace('\\n',' ')
clean1 = list(str(clean).split(' '))[9:]
print(clean1)
temp = defaultdict(list)
counter = 0
clean2 = []
for entry in clean1:
    try:
        int(entry)
        if int(entry) > 9:
            clean2.append(entry)
    except TypeError:
        clean2.append('#')
        clean2.append(entry)
        clean2.append('#')
    except ValueError:
        clean2.append(entry)
print(clean2)
# for j in clean2:
#     ''.join(j)
crosscheck = ['1', '2','3', '4', '5', '6', '7', '8', '9']
for index, i in enumerate(clean2, start=1):     
    if i[0] in crosscheck and i[-1] == '.':
        counter +=1 
    temp[counter].append(i)
print(temp)