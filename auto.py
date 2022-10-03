from selenium import webdriver
from time import sleep
import requests # to get image from the web
import shutil # to save it locally
import json
import os
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

driver.get('https://selfregistration.cowin.gov.in/')
sleep(2)

y=int(input())

name=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/ion-item/mat-form-field/div/div[1]/div/input')
name.send_keys(y)

login = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button')
login.click()

sleep(5)

y=int(input())

name=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[2]/ion-item/mat-form-field/div/div[1]/div/input')
name.send_keys(y)

login = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]/div/ion-button//button/span')
login.click()
