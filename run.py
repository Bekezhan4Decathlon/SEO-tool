import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')

def googleSearch(query, max_pages=5):
    row = []
    rows = []
    # search_bar = driver.find_element(By.NAME, 'q')
    # search_bar.send_keys(query)
    # search_bar.send_keys(Keys.RETURN)
    for n_page in range(1, max_pages):
        url = "http://www.google.com/search?q=" + query + "&start=" + str((n_page - 1) * 10)
        print(url)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('div', class_="yuRUbf")
        for i, link in enumerate(search):
            if "https://www.decathlonkz.com/" in link.a.get('href'):
                row.append(query)
                row.append(i)
                row.append(n_page)
        rows.append(row)
        row = []
    return rows

if __name__ == '__main__':
    driver.get('https://www.google.com/')
    time.sleep(5)
    organic_result = googleSearch('мячи kipsta алматы', 3)
    print(organic_result)



# query = 'Купить велосипеды в Алматы'
# links = []
# n_pages = 2 
# for page in range(1, n_pages):
#     url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     # soup = BeautifulSoup(r.text, 'html.parser')

#     search = soup.find_all('div', class_="TbwUpd NJjxre")
#     print(search)
#     print("______________")
#     print(type(search))
#     for h in search:
#         links.append(h.a.get('href'))

# print(links)