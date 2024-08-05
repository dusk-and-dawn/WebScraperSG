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
print(x)
