import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def analyzeSector(url):
    print(url)

def fetchSectors(sectors):
    for sector in sectors:
        analyzeSector(sector['Index_Name'])

def initializeAnalysis(url):

    #Using Selenium
    '''
    browser = webdriver.Firefox()
    browser.get(url)
    delay = 5 #seconds
    WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_element_by_id('mktrounddiv_2')))
    browser.find_element_by_id("mktrounddiv_2").click()
    html_source = browser.page_source
    #browser.quit()
    '''
    #Using BeautifulSoup
    '''
    page = requests.get(url).text
    soup = BeautifulSoup(html_source,"html.parser")
    sector = soup.find('table','tblgblmkt')
    sectorSection = soup.find('div', id="mktrounddiv_2").find_next('table', 'tblgblmkt')
    print(sectorSection)
    '''
    response = requests.get(url).text
    sectors = json.loads(response)
    fetchSectors(sectors)

url = "http://www.moneycontrol.com/mccode/markets/hotstocks/mkt_sector.json"
initializeAnalysis(url)
