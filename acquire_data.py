from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from db import send_to_db, get_from_db
from datetime import datetime 
from scrape_more import scraping_way_back, scraping_precise, scraping_broad
from test import clean_up
from scrape_all_approach import scrape_current_day

# 2015 - 2016
snapshots = [
    #'20150213020035', here different format
    #'20150315063000', same
    #'20150415033839', 
    #'20150515144023',
    #'20150615082347',
    #'20150716072943',
    '20150924003236',
    '20151025034147'
    ]

# 2017 - 2019
simple_snapshots = [
    '20190325082923',
    '20180717123539',
    '20181104041242',
    '20170512121814',
    '20170613135845',
    '20170716073915',
    '20170816010622' #,
    #'20171220140301'
    ]

# 2020

def string_maker(snapshot):
    x = 'https://web.archive.org/web/' + snapshot + '/https://www.sofascore.com/tennis/rankings/wta'
    return x

def run15_16(list):
    counter = 0 
    for snapshot in list:
        fst = string_maker(snapshot)
        print(f'{counter} made a string: {fst}')
        snd = scraping_broad(fst, 'js-list-filter-items')        
        print(f'scraped new snapshot {snapshot}')
        trd = clean_up(snd)
        print(f'cleaned the data {trd}')
        fth = send_to_db(snapshot, trd)
        print(f'{counter} sent it to the db')
        counter += 1
    print('collected 2015 - 2016 snapshot data successfully')

def run17_19(list):
    counter = 0
    for snapshot in list:
        fst = string_maker(snapshot)
        print(f'{counter} made a string: {fst}')
        snd = scraping_way_back(fst)
        print(f'{counter} scraped data succesfully{snd}')
        trd = send_to_db(snapshot, snd)
        print(f'{counter} sent it to the db {snd}')
        counter += 1
    print('collected 2017 - 2019 snapshot data successfully')

def run20_21(list):
    counter = 0 
    for snapshot in list:
        fst = string_maker(snapshot)
        print(f'{counter} made a string: {fst}')
        snd = scraping_precise(fst, 'ReactVirtualized__Grid.ReactVirtualized__List', 'ReactVirtualized__Grid__innerScrollContainer', 'Content-sc-1o55eay-0.gYsVZh', 'Section-sc-1a7xrsb-0.hwkKwf','Content-sc-1o55eay-0.gYsVZh', 'Content-sc-1o55eay-0.gYsVZh')        
        print(f'scraped new snapshot {snapshot}')
        trd = send_to_db(snapshot, snd)
        print(f'{counter} sent it to the db {snd}')
        counter += 1
    print('collected 2020 - 2021 snapshot data successfully')

def read_csv_to_db(name, path):
    with open(path, 'r') as file:
        data = file.readlines()

    print(f'data: {data}')
    send_to_db(name, data)
    print('sent data to db')

def scrape_current(): 
    print('start current day scraping')
    fst = scrape_current_day('https://www.sofascore.com/tennis/rankings/wta')
    print(f'current day scraped {fst}')
    send_to_db('wtaMasterList', fst)
    print('sent current day data to db')

'''
CONTROL HUB
'''
#run15_16(snapshots)
#run17_19(simple_snapshots)
#run20_21(['20200318145554'])
#scrape_current()

#read_csv_to_db('population_data','/home/a_mind/Downloads/population-and-demography.csv')

