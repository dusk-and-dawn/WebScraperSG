from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from db import send_to_db, get_from_db
from datetime import datetime 
from scrape_more import scraping_way_back, scraping_precise

# 2015
snapshots = [
    '20150213020035',
    '20150315063000', 
    '20150415033839', 
    '20150515144023',
    '20150615082347',
    '20150716072943',
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
    '20170816010622',
    '20171220140301'
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
        snd = scraping_precise(fst, 'layout-column-main', 'card', 'cell__content.h4', 'cell__section.main.cell__content.h4','cell__content.u-tDim', 'cell__section.u-pH12.u-tR.u-w72.cell__content')        
        print(f'scraped new snapshot {snapshot}')
        trd = send_to_db(snapshot, snd)
        print(f'{counter} sent it to the db {snd}')
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
'''
CONTROL HUB
'''
#run15_16(snapshots)
run20_21(['20200318145554'])