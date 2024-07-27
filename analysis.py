

import json
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

'''
ATTENTION! 
Make sure to run the scraper first, as this requires a json file of the name wta500.json in the active directory, which you get from running the scraper. 
'''
#load data 
with open('wta500.json', 'r', encoding='utf-8') as file:
    allList = json.load(file)

columns = ['Rank', 'Player', 'Country', 'Points']
df = pd.DataFrame(allList, columns=columns)
df['Rank'] = pd.to_numeric(df['Rank'])
df['Points'] = pd.to_numeric(df['Points'])

#print(df.head())  
print(df['Country'].head())

#preparation for grafics
hm = {}
for i in df['Country']:
    pass
    if i in hm.keys():
        hm[i] += 1
    else:
        hm[i] = 1

#print(hm) 
countries_ranked = sorted(hm.items(), key=lambda x:x[1])[::-1]
#print(countries_ranked)
countries = [i[0] for i in countries_ranked]
appearances = [i[1] for i in countries_ranked]
print(countries, appearances)

#creating the grafic
fig, ax = plt.subplots(figsize=(20,10))
ax.barh(countries, appearances)
ax.invert_yaxis()
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)
plt.show()


