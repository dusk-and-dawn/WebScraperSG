from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#/home/a_mind/code/WebScraperSG/tennis_venv/lib/python3.10/site-packages/selenium/webdriver/chrome/__pycache__/webdriver.cpython-310.pyc
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com/')
print('network access success')

driver.get('http://web.archive.org/web/20190307025257/https://www.sofascore.com/tennis/rankings/wta')
print('archive reached')

text_box = driver.find_element(by=By.CLASS_NAME, value='js-list-filter-items')

stuff = text_box.text.split()

#print(text_box.text)

print(stuff)
data = []
temp = text_box.find_elements(By.CLASS_NAME, 'js-list-filter-item')

for element in temp:
    try:
        rank = element.find_element(By.CLASS_NAME, 'cell__content.h4').text
        name = element.find_element(By.CLASS_NAME, 'cell__content.ff-medium.js-list-filter-value').text
        country = element.find_element(By.CLASS_NAME, 'cell__content.u-tDim').text
        points = element.find_element(By.CLASS_NAME, 'cell__section.u-pH12.u-tR.u-w72').text
        data.append([rank, name, country, points])
    except Exception as e:
        print(f'fail {e}')
        continue

# for index, element in enumerate(stuff):
#     if index % 5 == 0 and index != 0:
#         temp.append(element)
#         data.append(temp)
#         temp = []
#     else:
#         temp.append(element)
driver.close()
print(data)

