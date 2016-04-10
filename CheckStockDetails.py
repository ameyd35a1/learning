import requests
from bs4 import BeautifulSoup
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

URL = []

with open('stocks.json') as stocks_json:
    data_file = json.load(stocks_json)


for data in data_file['stocks']:
    URL.append(data['url'])

def getSentiments(soup):
    """
    Gets the sentiments of the users on the stock
    """
    try:
        sentiments_buy = soup.find('span','pl_bar brdwr')['style'].replace('width:','')
    except:
        sentiments_buy = ''
    try:
        sentiments_sell = soup.find('span','pl_bar brdwr rd')['style'].replace('width:','')
    except:
        sentiments_sell = ''
    try:
        sentiments_hold = soup.find('span','pl_bar hold')['style'].replace('width:','')
    except:
        sentiments_hold = ''
    sentiments = ''

    if sentiments_buy is not 'None' and sentiments_buy is not '':
        sentiments =  sentiments + bcolors.OKGREEN + sentiments_buy + bcolors.ENDC +" "

    if sentiments_hold is not 'None' and sentiments_hold is not '':
        sentiments =  sentiments + bcolors.WARNING + sentiments_hold + bcolors.ENDC +" "

    if sentiments_sell is not 'None' and sentiments_sell is not '':
        sentiments =  sentiments + bcolors.FAIL + sentiments_sell + bcolors.ENDC +" "

    return sentiments

def getMarketStatus(soup):
    """
    Gets the trading activity on the stock
    """
    status = soup.find(id = 'md_name')['class']
    marketStatus = ''
    if 'gL_10' in status:
        marketStatus = 'NEUTRAL'
    elif 'r_10' in status:
        marketStatus = 'SELL'
    elif 'gr_10' in status:
        marketStatus = 'BUY'

    return marketStatus


def getStockDetails(url):
    page = requests.get(url).text
    #Bse_Prc_tick
    soup = BeautifulSoup(page,"html.parser")
    bseVal = soup.select("#Bse_Prc_tick strong")[0].contents[0]
    nseVal = soup.select("#Nse_Prc_tick strong")[0].contents[0]
    riseBseVal = soup.select("#b_changetext strong")[0].contents[0]
    riseNseVal = soup.select("#n_changetext strong")[0].contents[0]
    directionBse = soup.find('div',id="b_changetext").span['class']
    directionNse = soup.find('div',id="n_changetext").span['class']
    sentiments_buy = sentiments_sell = sentiments_hold = colorBse = colorNse = ''
    title = soup.find('h1','b_42').contents[0]

    sentiments = getSentiments(soup)
    buy_sell_status = getMarketStatus(soup)

    if 'uparw_pc' in directionBse:
        directionBse = 'UP'
        colorBse = bcolors.OKGREEN
    else:
        directionBse = 'DOWN'
        colorBse = bcolors.FAIL

    if 'uparw_pc' in directionNse:
        directionNse = 'UP'
        colorNse = bcolors.OKGREEN
    else:
        directionNse = 'DOWN'
        colorNse = bcolors.FAIL

    print(bcolors.BOLD+ title+ bcolors.ENDC)
    print ("BSE: "+bseVal +" "+ colorBse + riseBseVal + bcolors.ENDC + " "+ directionBse)

    print ("NSE: "+nseVal +" "+ colorNse +riseNseVal + bcolors.ENDC + " "+ directionNse)

    if sentiments is not '':
        print("Sentiments: " + sentiments )

    print('Market status: ' + buy_sell_status )
    print ('\n')


for url in URL:
    getStockDetails(url)
'''
page = requests.get("http://www.moneycontrol.com/india/stockpricequote/refineries/indianoilcorporation/IOC").text
soup = BeautifulSoup(page,"html.parser")
status = soup.find(id = 'md_name')['class']
print(status)
'''
#def analysis(url):
