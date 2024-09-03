import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_navigation import open_website, scroll_by_pixels
from db import get_from_db

x = get_from_db('20150213020035')
#print(x['content'])

def clean_up(list):
    data = []
    for i in range(1, 350):
        rank_index = list.index(str(i))
        end_index = list.index(str(i+1))
        print(rank_index, end_index)
        if end_index < rank_index:
            list.pop(end_index)
            rank_index = list.index(str(i))
            name = list[rank_index+1], list[rank_index+2]
            country = list[rank_index +3]
            try:
                points = int(list[rank_index+4])
                if points < 50:
                    points = int(list[rank_index+5]) 
            except:
                try:
                    points = int(list[rank_index+5])
                    if points < 50:
                        points = int(list[rank_index+6])
                except:
                    points = int(list[rank_index+6])
                    if points < 50:
                        points = int(list[rank_index+7])
        else:
            
            rank = int(list[rank_index])
            name = list[rank_index+1], list[rank_index+2]
            country = list[rank_index +3]
            try:
                points = int(list[rank_index+4])
                if points < 50:
                    points = int(list[rank_index+5])
            except:
                try:
                    points = int(list[rank_index+5])
                    if points < 50:
                        points = int(list[rank_index+6])
                except:
                    points = int(list[rank_index+6])
                    if points < 50:
                        points = int(list[rank_index+7])

        data.append([rank, name, country, points])
    print(data)
    return data

#clean_up(x['content'])