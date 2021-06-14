# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:36:13 2021

@author: Hp EliteDesk 705 G3
"""

#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

user_name = "esjay2020"
password = ""

def load_page():
    driver = webdriver.Chrome(r'C:\CEH\chrom_driver\chromedriver.exe')
   
    driver.get("http://www.instagram.com")
    return driver


def login(user_name,password,driver):
    username_txt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_txt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username_txt.clear()
    username_txt.send_keys(user_name)
    password_txt.clear()
    password_txt.send_keys(password)
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


def search(keyword):
    
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()
    print(searchbox)
    
    #search for the hashtag cat
    key_word = keyword
    searchbox.send_keys(key_word)
    time.sleep(1)
    searchbox.send_keys(Keys.ENTER) 
    searchbox.send_keys(Keys.ENTER) 
   

        
def scroll(tag):
     
       body = driver.find_element_by_tag_name('body')
       if tag == 'up':
           body.send_keys(Keys.PAGE_UP)
       else:
           body.send_keys(Keys.PAGE_DOWN)
           
frined_status=[]
frined_status = driver.find_elements_by_css_selector('li.Ckrof')   
miss=frined_status[1].find_element_by_xpath("//canvas[@class='CfWVH']")  




#react-root > section > main > section > div.cGcGK > div.zGtbP.IPQ5.VideM > div > div > div > div > ul > li:nth-child(4) > div > button > div.RR-M-.QN629 > canvas