

import json
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt


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
#print(df['Country'].head())

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
#print(countries, appearances)

#creating the grafic

fig, ax = plt.subplots(figsize=(20,10))
ax.barh(countries[:20], appearances[:20])
ax.invert_yaxis()
ax.set_title('countries representation in the WTA rankings top 500',
             loc='left', )
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.xaxis.set_tick_params(pad=10)
ax.yaxis.set_tick_params(pad=10)
plt.savefig('top20_wta500_countries_ranked_by_appearance')
plt.show()


# Second Chapter countries representation in Top 100 
hm100 = {}


for index, country in enumerate(df['Country']):
    if index < 101:
        if country in hm100.keys():
            hm100[country] += 1
        else:
            hm100[country] = 1

countries100_ranked = sorted(hm100.items(), key=lambda x:x[1])[::-1]

countries100 = [i[0] for i in countries100_ranked]
appearances100 = [i[1] for i in countries100_ranked]

fig100, ax100 = plt.subplots(figsize=(20,10))
ax100.barh(countries100[:20], appearances100[:20])
ax100.invert_yaxis() 
ax100.set_title('countries representation in the WTA rankings top 100',
             loc='left', )
plt.savefig('top20_wta100_countries_ranked_by_appearance')
plt.show()

#print(countries100, appearances100)
for i in range(20):
    print(countries[i], countries100[i])
    if countries[i] not in countries100[:20]:
        print(f'this country is in the top 20 when looking at top 500 but not if one only looks at the top 100: {countries[i]}')
    if countries100[i] not in countries[:20]:
        print(f'this country is in the top 20 when looking at top 100 but not if one only looks at the top 500: {countries100[i]}')

# comparison bar chart 
comparison = {'top500': [i for i in appearances[:20]],
              'top100': [i for i in appearances100[:20]]}
indexprep = []
for i in range(20):
    x = str(countries[i]) + ' | ' + str(countries100[i])
    indexprep.append(x)

comp_df = pd.DataFrame(comparison, columns=['top500', 'top100'], index=indexprep)

comp_df.plot.barh(figsize=(20, 10), title='comparison of top 20 countries based on ranks in top 500 and top 100 WTA').invert_yaxis()


plt.show()