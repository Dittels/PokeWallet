from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook, Workbook
import io
import requests
import time
import shutil
import os

def URLScrape(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(15)
    cardName = driver.find_element(By.CLASS_NAME, "product-details__name").text
    cardPrice = driver.find_element(By.CLASS_NAME, "price").text
    cardPrice = float(cardPrice[1:])

    driver.close()
    return cardName, cardPrice
    
def CardUpdate():
    print(1)